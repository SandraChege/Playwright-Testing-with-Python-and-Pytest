from playwright.sync_api import Page, expect
from utilities.constants import BASE_URL
import random

def test_savings_tab_title(page:Page):
    page.goto(f'{BASE_URL}savings.html')
    expect(page).to_have_title("Save with us")

def test_user_is_in_savings_tab(page:Page):
    page.goto(f'{BASE_URL}savings.html')
    savings_tab = page.locator('.nav-item').nth(1)
    expect(savings_tab).to_have_text("Savings")

def test_saving_tab_heading(page:Page):
    page.goto(f'{BASE_URL}savings.html')
    heading = page.get_by_role("heading", level=4).nth(0)
    expect(heading).to_have_text("Deposit your money with us to earn a great yield")

def test_savings_deposit_form(page:Page):
    page.goto(f'{BASE_URL}savings.html')

    # Verify the deposit input field
    expect(page.get_by_label('How much you wish to deposit')).to_be_visible()
    expect(page.locator('#deposit')).to_be_editable()

    # Verify the time period dropdown
    expect(page.get_by_label('Time Period')).to_be_visible()
    period_dropdown = page.locator('#period')
    options = period_dropdown.get_by_role('option').all()

    for option in options:
        value = option.get_attribute("value")  
        period_dropdown.select_option(value)
        expect(period_dropdown).to_have_value(value)

def test_savings_current_rates_table(page:Page):
    page.goto(f'{BASE_URL}savings.html')
    heading = page.get_by_role("heading", level=4).nth(1)
    expect(heading).to_have_text("Current rates (yearly yield)")

    table = page.get_by_role('table') #locate the table
    #verify the headers
    headers =  table.locator("thead tr td").all_text_contents()
    expected_headers = ["", "6 months", "1 year", "2 years"]
    assert headers == expected_headers, f"Expected headers {expected_headers}, but got {headers}"

    rows = table.locator("tbody tr").all()

    # Expected rows
    expected_data = [
        ["Us", "4%", "5%", "6%"],
        ["Competition", "2%", "3%", "4%"]
    ]

    for i, row in enumerate(rows):
        cells = row.locator("td").all_text_contents()
        assert cells == expected_data[i], f"Expected {expected_data[i]}, but got {cells}"


def test_savings_calculation(page:Page):
    page.goto(f'{BASE_URL}savings.html')

    # Ensure the result field is initially empty
    result_field = page.locator('#result')
    expect(result_field).to_be_empty()

    # Generate a random deposit amount between 100 and 10,000
    random_deposit = random.randint(100, 10000)

    # Locate and fill the deposit input field with the random value
    deposit_input = page.locator('#deposit')
    expect(deposit_input).to_be_visible()
    deposit_input.fill(str(random_deposit))  # Convert to string for input field

    # Locate the period dropdown and get all available options
    period_dropdown = page.locator('#period')
    option = period_dropdown.get_by_role('option').nth(1)
    time_period = option.get_attribute("value")

    period_dropdown.select_option(time_period)

    # Find the corresponding interest rate from the table (1-year is column 3)
    rate_cell = page.locator("#rates tbody tr:first-child td:nth-child(3)")
    rate_text = rate_cell.inner_text().strip('%')  # Convert "5%" to "5"
    interest_rate = float(rate_text) / 100  # Convert to decimal (0.05)

    # ✅ Correct calculation for interest earned
    expected_interest = random_deposit * interest_rate

    # ✅ Expected text format
    expected_text = f"After {time_period} you will earn ${expected_interest:.2f} on your deposit"

    # Verify the result text matches the expected calculation
    expect(result_field).to_have_text(expected_text)
    print(f"Test passed with random deposit: {random_deposit}")

def test_savings_download_button(page:Page):
    page.goto(f'{BASE_URL}savings.html')
    download_button = page.get_by_role("button")
    expect(download_button).to_contain_text('Download Our Offer')
    download_button.click()
    expect(page).to_have_url(f'{BASE_URL}files/dummy.pdf')
    page.go_back()