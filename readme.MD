# Playwright Learning Guide

## Introduction
Playwright is a powerful end-to-end testing framework that enables automated testing of web applications across different browsers. It supports **Chromium, Firefox, and WebKit**, and provides features like network interception, tracing, and parallel execution.

## Installation
Ensure you have **Python** installed, then install Playwright using pip:

```sh
pip install playwright
playwright install
```

## Running Your First Test
Create a test file (e.g., `test_example.py`) and write a simple test.

### **Python Example**:
```python
from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.fill("input[name='q']", "Playwright testing")
        page.press("input[name='q']", "Enter")
        page.wait_for_timeout(3000)
        browser.close()
```

## Core Concepts
### **1. Browsers & Contexts**
- Playwright supports **Chromium, WebKit, and Firefox**.
- **Browser Contexts** allow testing multiple independent sessions in parallel.

```python
browser = playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()
```

### **2. Locators**
Playwright provides flexible ways to locate elements:

- `page.get_by_text("Register")`
- `page.get_by_role("button", name="Submit")`
- `page.get_by_label("Email")`
- `page.get_by_placeholder("Search")`
- `page.get_by_test_id("username-field")`

### **3. Assertions**
Playwright integrates with `expect` for assertions:
```python
from playwright.sync_api import expect

expect(page.locator("h1")).to_have_text("Welcome")
```

### **4. Running Tests**
Run Playwright tests using `pytest`:
```sh
pytest test_example.py
```

## Debugging Tips
- Use `headless=False` to see test execution.
- Use `.pause()` to interact with the browser manually.

## Resources
- [Playwright Docs](https://playwright.dev/python/)
- [GitHub Repo](https://github.com/microsoft/playwright-python)
- [Playwright Test Examples](https://github.com/microsoft/playwright-python/tree/main/examples)

---
Happy testing with Playwright! 🚀

