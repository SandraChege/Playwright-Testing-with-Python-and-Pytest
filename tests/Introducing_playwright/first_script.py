from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #Choose chrome as my browser
    browser =  playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/")
    browser.close()
