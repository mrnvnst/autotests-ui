import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
# Используем встроенную фикстуру playwright (установлена с плагином pytest-playwright)
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
