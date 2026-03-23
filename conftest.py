# подключение плагинов – указываем на файл с фикстурами, из к. pytest загрузит плагины
pytest_plugins = (
    "fixtures.browsers",
    "fixtures.pages",
)

