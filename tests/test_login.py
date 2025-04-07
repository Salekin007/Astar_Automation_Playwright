import pytest
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open_url("http://202.4.112.158/login")
    login_page.login("nurse", "123456")
    assert "dashboard" in page.url.lower(), "Login failed!"
