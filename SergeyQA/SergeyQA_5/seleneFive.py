import time

from selene import browser, have, command

browser.config.browser_name = "firefox"
browser.config.hold_browser_open = True

def test_hw():
    browser.open('https://demoqa.com/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('qaguru@mailto.plus')
    browser.all('.custom-radio').element_by(have.text('Female')).click()
    browser.element('#userNumber').type('+375')
    browser.element(".subjects-auto-complete__value-container").perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('English')
    browser.element('#react-select-2-option-0').click()