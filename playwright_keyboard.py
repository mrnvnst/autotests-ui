from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    # Устанавливаем фокус на поле Email (подготавливаем поле для ввода текста)
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in 'user@gmail.com':
        # Добавляем задержку 300 мс для имитации реального ввода (симуляция одиночного нажатия клавищ)
        page.keyboard.press(character, delay=300)

    # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    page.keyboard.press("ControlOrMeta+A")

    # Ждём 5 секунд для наглядности результата
    page.wait_for_timeout(5000)

    '''
    Метод page.keyboard.press() принимает:
        - Символы, например: a, 1, @.
        - Комбинации клавиш, например: ControlOrMeta+A, Shift+Enter.
        - Для одиночного нажатия клавищ – Enter, Tab
    
    Метод page.keyboard.type():
        - Имитация ввода текста символ за символ (видимо, в коде выше в цикле с побуквенным кодом
        лучше использовать именно этот метод)
        - Use when the page has special keyboard handling (e.g., auto-suggestions, real-time validation).
    
    Метод fill():
        - Recommended for most cases. Use for standard form filling.
    '''
