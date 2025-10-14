from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ждем полной загрузки страницы
    )

    # Выполняем JS-код для замены текста заголовка
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

    # Добавляем паузу для наглядности
    page.wait_for_timeout(5000)


"""
1. Метод page.evaluate:
Этот метод используется для выполнения JavaScript-кода на странице.

Пример выполняемого JS-кода:

// Находим заголовок по ID
const title = document.getElementById('authentication-ui-course-title-text');
// Изменяем его текст
title.textContent = 'New Text';

                  
2. Аргумент wait_until='networkidle':
Ждёт завершения загрузки всех сетевых запросов, чтобы гарантировать наличие нужного элемента в DOM. 
Без этого возможна ошибка, если элемент ещё не загрузился.
"""