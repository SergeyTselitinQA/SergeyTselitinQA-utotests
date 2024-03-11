import pytest
from selene import browser

@pytest.fixture()
def before_test():
    browser.config.browser_name = 'firefox'
    browser.config.window_width = 720
    browser.config.window_height = 960