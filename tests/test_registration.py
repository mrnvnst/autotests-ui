import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage
):
    # Вместо ручной инициализации браузера используем фикстуру
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_page.fill_registration_form(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.click_registration_button()
    # Переключение на POM Dashboard
    dashboard_page.check_visible_dashboard_title()


'''
запуск с учетом всей структуры на момент коммита:

python -m pytest tests/test_registration.py -s -v
'''

