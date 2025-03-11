from playwright.sync_api import Page
from utilities.constants import BASE_URL

def test_base_url_accessibility(page: Page):
    response = page.goto(BASE_URL)
    assert response is not None, "Failed to navigate to the base URL."
    assert response.status == 200, f"Expected status 200, but got {response.status}"

    print(f"Successfully accessed {BASE_URL} with status code {response.status}")