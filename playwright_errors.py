from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
              wait_until='networkidle')

    # Пытаемся проверить, что несуществующий локатор виден на странице
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    '''
    Анализ ошибки:
        1. AssertionError: Locator expected to be visible: скрипт ожидал, что локатор будет виден, но он не найден.
        2. LocatorAssertions.to_be_visible with timeout 5000ms: playwright пытался найти локатор в течение 5 секунд.
        3. waiting for locator("#unknown"): playwright искал локатор с ID #unknown.
    '''

    # Пытаемся ввести текст в кнопку Login
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    '''
    Анализ ошибки:
        1. waiting for get_by_test_id("login-page-login-button"): playwright нашел локатор кнопки.
        2. Locator resolved to <button>...: элемент успешно найден, 
        но его свойства (например, disabled) не позволяют выполнить действие.
        3. element is not enabled: playwright ожидал, что элемент станет активным и доступным для взаимодействия, 
        но этого не произошло.
    '''

    # Пытаемся изменить текст заголовка
    page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """)

    '''
    Анализ ошибки:
        TypeError: Cannot set properties of null: элемент не найден, так как не успел загрузиться.
        Такое случается в динамических приложениях (SPA), 
        где элементы появляются только после завершения сетевых запросов или выполнения JS-скриптов.
    '''

