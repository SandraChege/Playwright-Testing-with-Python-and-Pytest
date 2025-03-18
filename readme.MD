# Playwright Learning Guide 🎭🚀📜

## 1. Introduction 🎯🔍✨
Playwright is a powerful end-to-end testing framework that enables automated testing of web applications across different browsers. It supports **Chromium, Firefox, and WebKit**, and provides features like network interception, tracing, and parallel execution.

---

## 2. Installation 🛠️📦💡
Ensure you have **Python** installed, then install Playwright using pip:

```sh
pip install playwright
playwright install
```

---

## 3. Running Your First Test 🏁🎬✅
Create a test file (e.g., `test_example.py`) and write a simple test.

### **Python Example:**
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

---

## 4. Core Concepts 🏗️🧠💡
### **1️⃣ Browsers & Contexts**
- Playwright supports **Chromium, WebKit, and Firefox**.
- **Browser Contexts** allow testing multiple independent sessions in parallel.

```python
browser = playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()
```

### **2️⃣ Locators**
Playwright provides flexible ways to locate elements:

- `page.get_by_text("Register")`
- `page.get_by_role("button", name="Submit")`
- `page.get_by_label("Email")`
- `page.get_by_placeholder("Search")`
- `page.get_by_test_id("username-field")`

### **3️⃣ Assertions**
Playwright integrates with `expect` for assertions:
```python
from playwright.sync_api import expect

expect(page.locator("h1")).to_have_text("Welcome")
```

### **4️⃣ Running Tests**
Run Playwright tests using `pytest`:
```sh
pytest test_example.py
```

### **5️⃣ Basic Actions**
Playwright provides methods to navigate web pages effectively:
- `page.goto(url)`: Navigates to a specified URL.
- `page.go_back()`: Moves to the previous page in history.
- `page.go_forward()`: Advances to the next page in history.
- `page.reload()`: Reloads the current page.

#### ⏳ Waiting for Page Load
You can use the `wait_until` parameter to control when navigation is considered complete. Available options:
- `commit` – Navigation committed.
- `domcontentloaded` – DOM content fully loaded.
- `load` – Page fully loaded (including resources like images and scripts).
- `networkidle` – No ongoing network requests.

### **6️⃣ Difference between `fill()` vs `type()`**
Both `fill()` and `type()` are used to enter text into input fields, but they behave differently:
- `fill(value)`:
  - Clears existing text before entering new value.
  - Faster as it sets the value directly.
- `type(value)`:
  - Simulates real typing, one character at a time.
  - Slower but mimics user input.
  - Does not clear existing value.
Use `fill()` when you just want to set a value quickly, and `type()` when simulating real user input with keypress events.

---

# 5. Handling Date Pickers in Playwright 📅⌨️🕒

## Introduction 📝🖱️🛠️
This document provides guidelines on how to interact with date pickers in Playwright. Depending on the implementation of the date picker, different approaches may be required to select a date.

### **1️⃣ Filling a Native HTML Date Input**
✅ Best for `<input type='date'>`
If the date picker is a standard HTML date input, you can directly set its value using `.fill()`.

#### **Example:**
```python
page.locator("input[type='date']").fill("2025-03-12")  # Format: YYYY-MM-DD
expect(page.locator("input[type='date']")).to_have_value("2025-03-12")
```
📌 **Format Required:** `YYYY-MM-DD`

### **2️⃣ Clicking Through a JavaScript-Based Date Picker**
✅ Best for Date Pickers with Popups
If the date picker opens a calendar popup, use **click actions** to select a date.

#### **Example:**
```python
page.get_by_placeholder("Select Date").click()  # Open the calendar popup
page.get_by_text("12").click()  # Click on the 12th day
expect(page.get_by_placeholder("Select Date")).to_have_value("03/12/2025")  # Format may vary
```
📌 This approach **mimics a real user** clicking through the UI.

### **3️⃣ Setting a Date Using JavaScript (For Complex Pickers)**
✅ Best for JavaScript-Based Date Pickers
If `.fill()` does not work, you can use JavaScript to **directly set the date value**.

#### **Example:**
```python
page.evaluate("document.querySelector('input[type=date]').value = '2025-03-12'")
expect(page.locator("input[type='date']")).to_have_value("2025-03-12")
```
📌 This method **bypasses UI interactions**, setting the value directly in the DOM.

### 📌 Choosing the Right Approach
| **Scenario** | **Best Approach** |
|-------------|----------------|
| Standard `<input type='date'>` | Use `.fill("YYYY-MM-DD")` |
| Popup-based calendar | Click input → Select date |
| Complex JavaScript date pickers | Use `.evaluate()` to set value |

### ✅ Verifying the Date Selection
To check the selected date value, you can print it:
```python
value = page.evaluate("document.querySelector('input[type=date]').value")
print(value)  # Output: '2025-03-12'
```

---

## 6. Debugging Tips 🔍🛠️🐞
- Use `headless=False` to see test execution.
- Use `.pause()` to interact with the browser manually.

## 7. Resources 📚🔗🌐
- [Playwright Docs](https://playwright.dev/python/)
- [GitHub Repo](https://github.com/microsoft/playwright-python)
- [Playwright Test Examples](https://github.com/microsoft/playwright-python/tree/main/examples)

---

Happy testing with Playwright! 🚀🎉😃

