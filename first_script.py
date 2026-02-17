import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    new_context = browser.new_context()
    page = new_context.new_page()
    page.goto("http://192.168.1.79:5000/login")
    print(page.url)
    time.sleep(2)
    print(f"Sample value:{page.get_by_role("textbox",name="sample_text").input_value()}")
    print("Is Sample Credentials present on the page? ", page.get_by_text("Sample Credentials").is_visible())
    # print(f"PageByRole Header: {page.get_by_role("heading").inner_text()}")
    # xpath_selector_text = page.locator("//h1[@data-testid='home-title']").inner_text()
    # print(f"Xpath Header: {xpath_selector_text}")
    page.get_by_role("textbox", name="email").type("admin@test.com")
    #page.get_by_role("textbox", name="password").type("Password123")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Login").click()

    #page.screenshot(path="first_screenshot.png")
    print(f"Success message:{page.get_by_role("alert").inner_text()}")

    # IFrame
    page.goto("http://192.168.1.79:5000/iframe")
    print(page.url)

    browser.close()