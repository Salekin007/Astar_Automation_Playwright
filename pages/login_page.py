from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = "input[placeholder='Username']"
        self.password_input = "input[placeholder='Password']"
        self.login_button = "button[type='submit']"

    def login(self, username: str, password: str):
        """Performs login with given credentials."""
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.page.press(self.password_input, "Enter")
