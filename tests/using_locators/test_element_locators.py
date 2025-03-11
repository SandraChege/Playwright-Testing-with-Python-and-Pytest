from playwright.sync_api import Page, expect
from utilities.constants import BASE_URL

'''
Locators using Roles
<button id="register" class="btn btn-primary btn-lg" type="submit"> Register </button>
1. In the first method we have saved first_name since we can reuse agin
2. In the second method for lat name and email we will not reuse them again
Exact makes locator case sensitive and demands the sting to match the name. 
'''

def test_locators_by_role(page:Page):
    page.goto(BASE_URL)

    page.get_by_label('First name').fill("Sandra")
    page.get_by_label('Last name').fill("Chege")
    page.get_by_label('Email').fill("example@gmail.com")

    page.get_by_role("button", name= 'Register', exact= True).click()

'''
Locators using text
'''
def test_locaors_by_text(page:Page):
    page.goto(BASE_URL)
    
    page.get_by_role("button", name= 'Register', exact= True).click()
    warning = page.get_by_text('Valid first name is required')
    expect(warning).to_be_visible()
    assert warning.evaluate("element => getComputedStyle(element).color") == "rgb(220, 53, 69)", "Warning text is not red!"

'''
Locators using Labels
<label for="firstName" class="form-label">First name</label>
1. In the first method we have saved first_name since we can reuse agin
2. In the second method for lat name and email we will not reuse them again
'''

def test_locators_by_label(page:Page):
    page.goto(BASE_URL)

    first_name = page.get_by_label('First name')
    first_name.fill("Sandra")

    page.get_by_label('Last name').fill("Chege")
    page.get_by_label('Email').fill("example@gmail.com")
'''
Filter function
'''
def test_filer(page:Page):
    page.goto(f'{BASE_URL}savings.html')

    rows = page.get_by_role('row')
    print(rows.count())

    row = page.get_by_role('row').filter(has_text="Competition")
    print(row.text_content())

    cell = page.get_by_role('row').filter(has_text="Competition").get_by_role('cell').nth(1)
    print(cell.text_content())
