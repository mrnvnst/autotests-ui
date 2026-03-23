import pytest

from playwright.sync_api import Page
from pages.login_page import LoginPage


# Инициализация страницы через фикстуру
@pytest.fixture
def login_page(chromium_page: Page) -> Page:
    return LoginPage(page=chromium_page)

