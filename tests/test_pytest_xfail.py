import pytest


@pytest.mark.xfail(reason='Найден баг в приложении, из-за которого тест падает с ошибкой')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='Баг уже исправлен, но на тест все еще висит маркировка xfail')
def test_without_bug():
    pass


@pytest.mark.xfail(reason='Внешний сервис временно недоступен')
def test_external_services_is_unavailable():
    assert 1 == 2


'''
Запуск автотеста:
python -m pytest -k "test_with_bug or test_without_bug or test_external_services_is_unavailable" -s -v

1. test_with_bug — XFAIL:
    Этот тест был помечен как ожидаемо провалившийся, потому что в коде есть известная ошибка.
    Тест провалился, но это expected failure – падение соответствует ожиданиям.

2. test_without_bug — XPASS:
    Этот тест помечен как ожидаемо провалившийся, но тест прошёл успешно
    pytest сообщает статус XPASS (unexpected pass — неожиданный успешный результат). 
    Тест ожидался как проваленный, но он неожиданно прошел, потому что ошибка была исправлена.
    
3. test_external_services_is_unavailable — XFAIL:
    Тест ожидаемо провалился, как и ожидалось, из-за недоступности внешнего сервиса
'''