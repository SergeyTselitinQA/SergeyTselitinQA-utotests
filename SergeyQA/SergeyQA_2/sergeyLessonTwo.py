from selene import browser, have

browser.config.timeout = 6.0

def test_open_google(before_test):
    browser.open('https://google.com')
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element("h3").should(have.text('QA.GURU — Курсы тестировщиков - онлайн-обучение ...'))

def test_negativ(before_test):
    browser.open('https://google.com')
    browser.element('[name="q"]').type('098746324763473734383').press_enter()
    browser.element("//div[@class='v3jTId']").should(have.text('Похоже, по вашему запросу нет полезных результатов'))
