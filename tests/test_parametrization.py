import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(params=["chromium", "webkit", "firefox"])
# Фикстура будет возвращать три разных браузера – также и автотесты будут запускаться трижды
def browser(request: SubRequest) -> str:
    return request.param  # Внутри атрибута param находится одно из значений "chromium", "webkit", "firefox"


def test_open_browser(browser: str):
    # Используем фикстуру, котоаря вернет браузер в виде строки
    print(f"Running test on browser: {browser}")


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


'''
python -m pytest -k "test_numbers" -s -v

tests/test_parametrization.py::test_numbers[1] PASSED
tests/test_parametrization.py::test_numbers[2] PASSED
tests/test_parametrization.py::test_numbers[3] PASSED
tests/test_parametrization.py::test_numbers[-1] FAILED
'''


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


'''
python -m pytest -k "test_several_numbers" -s -v

tests/test_parametrization.py::test_several_numbers[1-1] PASSED
tests/test_parametrization.py::test_several_numbers[2-4] PASSED
tests/test_parametrization.py::test_several_numbers[3-9] PASSED

1. В декораторе @pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)]) 
указаны три набора параметров.

2. Названия аргументов number и expected должны совпадать с именами параметров функции test_several_numbers.

3. В квадратных скобках отображаются значения каждого набора параметров, с которыми запускался тест, 
что позволяет легко отследить, с какими данными работал каждый прогон.
'''


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0  # проверка для примера


'''
python -m pytest -k "test_multiplication_of_numbers" -s -v

Матрица из нескольких параметров – декартово произведение 
(каждый элемент 1-го множества комбинируется с каждым элементом второго множества)

Будет запущено 12 тестов.
'''