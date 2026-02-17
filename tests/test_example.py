from playwright.sync_api import sync_playwright
from src.pages.login_page import LoginPage


class TestExamples:
    def test_page_title(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://blisscoders.pythonanywhere.com/")

            assert "Playwright" in page.title()

            browser.close()

    def test_valid_login(self, playwright_page):
        login_page = LoginPage.open(page=playwright_page)
        login_page.login(username="admin@test.com",password="Password123")

    def test_invalid_login(self, playwright_page):
        login_page = LoginPage.open(playwright_page)
        login_page.login(username="test",password="123445")