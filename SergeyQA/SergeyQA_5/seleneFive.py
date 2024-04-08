from selene import browser, have

browser.config.browser_name = "firefox"
browser.config.hold_browser = True

def test_hw():
    browser.open('https://demoqa.com/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('qaguru@mailto.plus')
    browser.all('.custom-radio').element_by(have.text('Female')).click()
    browser.element('#userNumber').type('+375')