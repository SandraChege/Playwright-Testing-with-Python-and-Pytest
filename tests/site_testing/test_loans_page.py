from playwright.sync_api import Page, expect
from utilities.constants import BASE_URL

def test_loans_tab_title(page:Page):
    page.goto(f'{BASE_URL}loans.html')
    expect(page).to_have_title("Credit Association")

def test_user_is_in_loans_tab(page:Page):
    page.goto(f'{BASE_URL}loans.html')
    loan_tab = page.locator('.nav-item').nth(2)
    expect(loan_tab).to_have_text("Loans")

def test_loan_tab_heading(page:Page):
    page.goto(f'{BASE_URL}loans.html')
    heading = page.get_by_role("heading", level=4)
    expect(heading).to_have_text("Get a loan with us!")