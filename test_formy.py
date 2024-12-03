from playwright.sync_api import sync_playwright

def test_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://formy-project.herokuapp.com/form")


test_form()