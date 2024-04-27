# 1 Установка Selene
    # pip install selene --pre

# 2 Пример использования Selene
    # from selene import browser, have
    # browser.open('https://demoqa.com/automation-practice-form') открыть сайт
    # browser.should(have.title('DEMO')) проверка, что вкладка содержит текст 'DEMO'
    # browser.element('[class="main-header"]').should(have.text('Box')) Элемент по селектору «main-header» должен содержать текст «Box»