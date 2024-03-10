import pytest
from selene import browser, have
@pytest.fixture
def browser_settings():
    browser.config.window_width = 1000
    browser.config.window_height = 1000