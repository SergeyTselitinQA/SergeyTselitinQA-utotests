import pytest
from selene import browser, have
@pytest.fixture
def browser_settings():
    browser.config.window_width = 1000
    browser.config.window_height = 1000

def test_google_positive(browser_settings):
    browser.open("https://www.google.com/")
    browser.element("#APjFqb").type("yashaka/selene").press_enter()
    browser.element("[id=search]").should(have.text("yashaka/selene: User-oriented Web UI browser"))