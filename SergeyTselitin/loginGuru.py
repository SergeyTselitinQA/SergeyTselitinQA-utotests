from selene import browser, have

browser.config.hold_browser = True
browser.config.timeout = 6.0

def test_can_login():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type('Vit_3006_kon@mail.ru')
    browser.element('.login-form [name=password]').type('2fedaadd').press_enter()
    browser.element('#xdget642385_1').should(have.text('Здравствуйте, Vitali'))