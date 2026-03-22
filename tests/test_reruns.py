import random
import pytest


PLATFORM = "Linux"


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Перезапуск реализуется на уровне маркировки flaky
def test_reruns():
    assert random.choice([True, False])  # рандомный выбор True / False для демонстрации нестабильного теста


'''
плагин pytest-rerunfailures

reruns=3 — количество перезапусков. Если тест упадёт, он будет перезапущен до 3 раз.
reruns_delay=2 — задержка между перезапусками в секундах.

python -m pytest -k "test_reruns" -s -v

Результат выполнения с перезапуском:

tests/pytest/test_reruns.py::test_reruns RERUN
tests/pytest/test_reruns.py::test_reruns PASSED

RERUN — тест test_reruns изначально завершился неудачей 
(например, из-за нестабильности системы или временного сбоя) и был автоматически перезапущен 
благодаря плагину rerunfailures.
PASSED — после перезапуска тест успешно прошёл. Это демонстрирует, как перезапуск может помочь устранить 
временные или случайные сбои, не связанные с ошибками кода.
'''


# Использование для класса
@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])


# Перезапуск при выполнении условия
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([True, False])

