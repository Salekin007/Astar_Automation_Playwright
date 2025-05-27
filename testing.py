# import re
# from playwright.sync_api import Page, expect
#
# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")
#
#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))
#
# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")
#
#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()
#
#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

from tkinter.font import names

from playwright.sync_api import Page, expect


def test_UIChecks (page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_placeholder("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()