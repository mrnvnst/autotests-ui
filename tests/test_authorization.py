import pytest
from playwright.sync_api import expect, Page


login_data = {
    ("user.name@gmail.com", "password"): "Invalid email and password",
    ("user.name@gmail.com", "  "): "Invalid email and empty password",
    ("  ", "password"): "Empty email and invalid password"
}


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", login_data.keys(), ids=login_data.values())
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    # Теперь страница передаётся в тест через фикстуру 'chromium_page', браузер не нужно инициализировать вручную

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    test_wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(test_wrong_email_or_password_alert).to_be_visible()
    expect(test_wrong_email_or_password_alert).to_have_text("Wrong email or password")


'''
def test_wrong_email_or_password_authorization:(chromium_page: Page):
1. Удалена ручная инициализация браузера: Теперь не нужно использовать sync_playwright() и вручную создавать браузер
 и страницу, это делает фикстура chromium_page.
2. Фикстура chromium_page в параметрах теста: Тест принимает параметр chromium_page: Page, который автоматически
 предоставляет страницу, созданную через фикстуру.
3. Тест принимает параметр chromium_page: Page, который автоматически предоставляет страницу, созданную через фикстуру
'''