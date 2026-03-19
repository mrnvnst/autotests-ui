import pytest


@pytest.mark.skip(reason="Фича в разработке")  # Указываем маркировку, которая пропустит данный автотест
def test_feature_in_development():
    pass


'''
Запуск автотеста:
python -m pytest -k "test_feature_in_development" -s -v

1. Выбор теста по имени:
    - команда pytest -k "test_feature_in_development" -s -v запустила тест с фильтром
     по имени test_feature_in_development.
    - Pytest собрал 4 теста, но только один из них соответствовал этому имени.
    
2. SKIPPED в логе:
    - В логе, тест test_feature_in_development был пропущен (отмечен как SKIPPED)
    - Причина пропуска указана в скобках: (Фича в разработке). 
    Эта причина была передана в маркировке @pytest.mark.skip(reason="Фича в разработке")
'''

