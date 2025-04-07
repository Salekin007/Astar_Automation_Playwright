from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        """Opens a given URL."""
        self.page.goto(url)

    def enter_text(self, locator, text):
        """Fills an input field."""
        self.page.locator(locator).fill(text)

    def click(self, locator):
        """Clicks on an element."""
        self.page.locator(locator).click()
