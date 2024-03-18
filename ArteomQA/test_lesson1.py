from selene import browser, have


browser.config.hold_browser_open = True
browser.config.timeout = 8.0
def test_can_login():
    browser.open("https://school.qa.guru/cms/system/login?required=true")
    browser.element('div.login-form input[name=email]').type("qagurubot@gmail.com")
    browser.element("input[name=password]").type("somepasshere").press_enter()
    browser.element('div.logined-form').should(have.text("QA_GURU_BOT"))



