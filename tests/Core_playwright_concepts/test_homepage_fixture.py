from playwright.sync_api import Page, expect


def test_hoemapge_title(page: Page):
    page.goto('http://localhost:8000/')
    expect(page).to_have_title('Credit Association')
    

def test_hoemapge_title(page: Page):
    page.goto('http://localhost:8000/')
    page_title = page.locator('title')
    # assert page_title.text_content() == 'Credit Association'

    '''
    Due to latency we can use expect(). 
    expect() has an auto-retry i.e means looks for elemnt if not found in the initial search
    '''
    expect(page_title).to_contain_text('Credit Association')