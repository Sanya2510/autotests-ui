from playwright.sync_api import sync_playwright, Request, Response

def log_request(request: Request):  #  логирование запросов
    print(f'Request: {request.url}')

def log_response(response: Response):   #логирование ответов
    print(f'Response: {response.url}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)   #открываем браузер и создаем новую страницу
    page = browser.new_page()

    page.on('request', log_request)   #запрос отправлен
    page.on("response", log_response)   #ответ получен

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')   #переходим на страницу входа

    page.wait_for_timeout(5000)

