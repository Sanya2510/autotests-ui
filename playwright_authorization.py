from playwright.sync_api import sync_playwright, expect
'''
Цель:

Необходимо написать скрипт, который откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
Заполнит поле "Email" значением user.name@gmail.com
Заполнит поле "Password" значением password
Нажмет на кнопку "Login"
Проверит наличие алерта с текстом "Wrong email or password"

'''

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")


    page.wait_for_timeout(5000)


'''
Необходимо расположить блоки кода в правильном порядке. Скрипт должен выполнять следующие действия:

Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
Проверить наличие элементов: "Email", "Password", "Login"
Нажать на ссылку "Registration", после чего произойдет редирект на страницу Registration
Проверить наличие элементов: "Email", "Password", "Registration"

'''

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False) #запустили браузер
    page = browser.new_page() #запустили нвоую страницу

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login") #перешли по ссылке в новой странице

    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    # page.wait_for_timeout(5000)

    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.click()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()

    # page.wait_for_timeout(5000)








