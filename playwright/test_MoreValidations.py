from tkinter.font import names

from playwright.sync_api import Page, expect


def test_UIChecks (page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_placeholder("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()