from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    '''
    Меняем browser.new_page(), создававший странциу в общем (глобальном) контексте браузера.
    Все страницы в этом контексте разделяли данные сессии, cookies и local storage
    
    Сейчас используем метод browser.new_context(), который создаёт новый контекст.
    В нём можно открыть несколько страниц, которые будут иметь общие данные сессии
    (cookies, local storage, session storage и т. д.), но будут изолированы от других контекстов. 
    '''
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state_path='browser-state.json')
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    # dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_title).to_be_visible()
    # expect(dashboard_title).to_have_text("Dashboard")

    page.wait_for_timeout(5000)


