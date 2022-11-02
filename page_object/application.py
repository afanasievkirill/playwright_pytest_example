from playwright.sync_api import Playwright, expect

from page_object.group import Group


class App:
    """_summary_"""

    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url
        self.group = Group(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url == True:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def login(self, user: str, password: str):
        self.page.fill('input[name="user"]', user)
        self.page.fill('input[name="pass"]', password)
        self.page.get_by_role("button", name="Login").click()
        expect(self.page.locator(".header b")).to_have_text("(admin)")

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()
        expect(self.page.locator('input[name="user"]')).to_be_visible()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
