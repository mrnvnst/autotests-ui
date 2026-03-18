from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ждем полной загрузки страницы (завершения загрузки всех сетевых запросов)
    )

    '''
    Выполняем JS-код для замены текста заголовка
    1. Используем метод page.evaluate() для запуска JS
    2. Находим заголовок по ID:
        const title = document.getElementById('authentication-ui-course-title-text');
    3. Изменяем его текст:
        title.textContent = 'New Text';
    '''

    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

    # Добавляем паузу для наглядности
    page.wait_for_timeout(5000)

    '''
    Передача аргументов через анонимную функцию – предпочтительнее способа ниже: 
    защищает от ошибок форматирования строки
    
    page.evaluate(
        """
        (text) => { // Принимаем аргумент в JS функции
            const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = text;
        }
        """,
        'New Text'  # Передаём аргумент из Python
    )
    '''

    '''
    Форматирование строки в Python, альтернативный способ передачи аргумента:

    next_text = 'Another Text'
    page.evaluate(f"""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = '{next_text}';
    """)
    '''

