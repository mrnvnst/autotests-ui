import pytest


SYSTEM_VERSION = "v1.2.0"  # Для примера укажем версию тестируемой системы


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",  # Пропустим автотест, если версия системы равна v1.3.0
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():  # В текущей конфигурации этот тест запустится
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",  # Пропустим автотест, если версия системы равна v1.2.0
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():  # Этот автотест не запустится
    pass


'''
Запуск теста:
python -m pytest -k "test_system_version" -s -v

- Тест test_system_version_valid прошёл успешно (PASSED), потому что условие skipif не сработало
 (версия системы не равна v1.3.0).
- Тест test_system_version_invalid был пропущен (SKIPPED), потому что условие skipif сработало 
(версия системы — v1.2.0, что соответствует условию пропуска теста).
'''