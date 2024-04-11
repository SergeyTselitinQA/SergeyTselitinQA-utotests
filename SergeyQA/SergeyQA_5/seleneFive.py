from pathlib import Path
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
    browser.element('#userNumber').type('3753333333')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('2000')
    browser.element("//div[@class='react-datepicker__day react-datepicker__day--001']").click()

    browser.element(".subjects-auto-complete__value-container").perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('English')
    browser.element('#react-select-2-option-0').click()

    browser.element("[for='hobbies-checkbox-3']").perform(command.js.scroll_into_view)
    browser.element("[for='hobbies-checkbox-3']").click()

    browser.element('#uploadPicture').perform(command.js.scroll_into_view)
    browser.element('#uploadPicture').set_value(
        str(Path(__file__).parent.joinpath('resources/foto.jpg').absolute())
    )

    browser.element('#currentAddress').type('Беларусь, г. Орша, ул. Мира, д. 3')

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()

    browser.element('#submit').click()