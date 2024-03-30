from selene import browser

browser.config.timeout =  8.0

def test_hw():
    browser.open('https://demoqa.com/automation-practice-form')
