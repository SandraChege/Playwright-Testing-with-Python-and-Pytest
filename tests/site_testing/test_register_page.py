from playwright.sync_api import Page, expect
from utilities.constants import BASE_URL

def test_register_tab_title(page:Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Credit Association")

def test_user_is_in_register_tab(page:Page):
    page.goto(BASE_URL)
    register_tab = page.locator('.nav-item').nth(0)
    expect(register_tab).to_have_text("Register")

def test_user_navigation_to_other_tabs(page:Page):
    page.goto(BASE_URL)
    page.get_by_role('link', name="Savings", exact=True).click()
    expect(page).to_have_url(f"{BASE_URL}savings.html")

    page.get_by_role('link', name="Loans", exact=True).click()
    expect(page).to_have_url(f"{BASE_URL}loans.html")

def test_register_heading(page:Page):
    page.goto(BASE_URL)
    heading = page.get_by_role("heading", level=4)
    expect(heading).to_have_text("Register to become a member")

def test_form_validation(page:Page):
    page.goto(BASE_URL)
    page.get_by_role("button", name='Register', exact=True).click()
    expect(page.get_by_text('Valid first name is required')).to_be_visible()
    expect(page.get_by_text('Valid last name is required')).to_be_visible()
    expect(page.get_by_text('Please enter a valid email address')).to_be_visible()

def test_form_placeholder(page:Page):
    page.goto(BASE_URL)
    expect(page.get_by_placeholder('you@example.com')).to_be_visible()

def test_register_tab_email_validation(page:Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill('Sandra')
    page.get_by_label('Last name').fill('Chege')
    page.get_by_label('Email').fill('test')
    page.locator('#register').click()
    expect(page.get_by_text('Please enter a valid email address')).to_be_visible()

    page.get_by_label('Email').fill('test@')
    page.locator('#register').click()
    expect(page.get_by_text('Please enter a valid email address')).to_be_visible()

    page.get_by_label('Email').fill('test@g')
    page.locator('#register').click()
    expect(page.get_by_text('Please enter a valid email address')).not_to_be_visible()

def test_register_tab_date_picker(page: Page):
    page.goto(BASE_URL)
    page.evaluate("document.querySelector('input[type=date]').value = '2025-03-30'")
    expect(page.locator("input[type='date']")).to_have_value("2025-03-30")

def test_register_tab_checkbox_functionality(page:Page):
    page.goto(BASE_URL)
    page.get_by_role('checkbox').click()
    expect(page.get_by_role('checkbox')).to_be_checked()
    page.locator('#textarea').type('I had heard good things about your company from your colleague')

def test_register_tab_save_input_button_functionality(page: Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill('Sandra')
    page.get_by_label('Last name').fill('Chege')
    page.get_by_label('Email').fill('test@gmail.com')
    page.evaluate("document.querySelector('input[type=date]').value = '2025-03-30'")
    page.get_by_role('checkbox').click()
    page.locator('#textarea').type('I had heard good things about your company from your colleague')
    page.locator('#save').click()

    # Verify fields remain unchanged
    expect(page.get_by_label('First name')).to_have_value('Sandra')
    expect(page.get_by_label('Last name')).to_have_value('Chege')
    expect(page.get_by_label('Email')).to_have_value('test@gmail.com')
    expect(page.locator('input[type=date]')).to_have_value('2025-03-30')
    expect(page.get_by_role('checkbox')).not_to_be_checked() #The site remains checked after one clicks on save
    expect(page.locator('#textarea')).to_have_value('I had heard good things about your company from your colleague')

    page.locator('#clear').click()

def test_register_tab_register_button_functionality(page: Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill('Sandra')
    page.get_by_label('Last name').fill('Chege')
    page.get_by_label('Email').fill('test@gmail.com')
    page.evaluate("document.querySelector('input[type=date]').value = '2025-03-30'")
    page.get_by_role('checkbox').click()
    page.locator('#textarea').fill('I had heard good things about your company from your colleague')
    page.locator('#register').click()

    # Verify fields remain unchanged
    expect(page.get_by_label('First name')).to_have_value('')
    expect(page.get_by_label('Last name')).to_have_value('')
    expect(page.get_by_label('Email')).to_have_value('')
    expect(page.locator('input[type=date]')).to_have_value('')
    expect(page.get_by_role('checkbox')).not_to_be_checked() #The site remains checked after one clicks on save
    expect(page.locator('#textarea')).to_have_value('')

def test_register_tab_clear_button_functionality(page: Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill('Sandra')
    page.get_by_label('Last name').fill('Chege')
    page.get_by_label('Email').fill('test@gmail.com')
    page.evaluate("document.querySelector('input[type=date]').value = '2025-03-30'")
    page.get_by_role('checkbox').click()
    page.locator('#textarea').fill('I had heard good things about your company from your colleague')


    # Click the clear button and handle the confirmation dialog
    def handle_dialog(dialog):
        assert dialog.message == "This will clear all inputs. Continue?"
        dialog.accept()
    page.once("dialog", handle_dialog)

    page.locator('#clear').click()

    # Verify fields remain unchanged
    expect(page.get_by_label('First name')).to_have_value('')
    expect(page.get_by_label('Last name')).to_have_value('')
    expect(page.get_by_label('Email')).to_have_value('')
    expect(page.locator('input[type=date]')).to_have_value('')
    expect(page.get_by_role('checkbox')).to_be_checked() #The site remains checked after one clicks on clear
    expect(page.locator('#textarea')).to_have_value('')