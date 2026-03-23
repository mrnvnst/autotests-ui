import pytest
from playwright.sync_api import expect, Page

from pages.login_page import LoginPage

login_data = {
    ("user.name@gmail.com", "password"): "Invalid email and password",
    ("user.name@gmail.com", "  "): "Invalid email and empty password",
    ("  ", "password"): "Empty email and invalid password"
}


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", login_data.keys(), ids=login_data.values())
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    # Открываем страницу с помощью метода visit, наследуемого от BasePage
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Заполняем форму
    login_page.fill_login_form(email=email, password=password)
    # Нажимаем на кнопку Login
    login_page.click_login_button()
    # Проверям наличие сообщения об ошибке
    login_page.check_visible_wrong_email_or_password_alert()


'''
def test_wrong_email_or_password_authorization:(chromium_page: Page):
1. Удалена ручная инициализация браузера: Теперь не нужно использовать sync_playwright() и вручную создавать браузер
 и страницу, это делает фикстура chromium_page.
2. Фикстура chromium_page в параметрах теста: Тест принимает параметр chromium_page: Page, который автоматически
 предоставляет страницу, созданную через фикстуру.
3. Тест принимает параметр chromium_page: Page, который автоматически предоставляет страницу, созданную через фикстуру
'''