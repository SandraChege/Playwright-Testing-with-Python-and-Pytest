from playwright.sync_api import sync_playwright

'''
1. Place code inside a function.
2. The function prefix should be test
3. Use fixtures such page as to reduce boilerplate code
'''
def test_homepage():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto('http://localhost:8000/')
            page.screenshot(path=f'example-{browser_type.name}.png')
            browser.close()