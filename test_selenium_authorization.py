import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

def test_authorization(selenium):
    """ Авторизация пользователя (UI)"""

    # Откроем сайт Ростелеком:
    selenium.get('https://b2c.passport.rt.ru/')
    time.sleep(5)
    # Находим заголовок "Авторизация" по имени класса:
    search_auth = selenium.find_element(By.CSS_SELECTOR, 'h1.card-container__title')
    time.sleep(5)
    # Находим Таб выбора аутентификации по номеру телефона, "Телефон":
    search_phone = selenium.find_element(By.ID, 't-btn-tab-phone')
    time.sleep(5)
    # Находим Таб выбора аутентификации по логину и паролю, "Почта":
    search_mail = selenium.find_element(By.ID, 't-btn-tab-mail')
    time.sleep(5)
    # Находим Таб выбора аутентификации по почте и паролю, "Логин":
    search_login = selenium.find_element(By.ID, 't-btn-tab-login')
    time.sleep(5)
    # Находим Таб выбора аутентификации по лицевому счету и паролю, “Лицевой счет”:
    search_ls = selenium.find_element(By.ID, 't-btn-tab-ls')
    time.sleep(5)
    # Находим поле ввода "Мобильный телефон":
    search_input_username = selenium.find_element(By.ID, 'username')
    # Находим поле ввода "Пароль":
    search_input_password = selenium.find_element(By.ID, 'password')
    # Находим кнопку "Войти":
    search_button_login = selenium.find_element(By.ID, 'kc-login')
    # Находим Чек-бокс "Запомнить меня":
    search_checkbox = selenium.find_element(By.CSS_SELECTOR, 'span.rt-checkbox__shape.rt-checkbox__shape--circular.rt-checkbox__shape--orange')
    # Находим Ссылку "Забыл пароль":
    search_button_forgot_password= selenium.find_element(By.ID, 'forgot_password')
    # Находим Ссылку на Пользовательское соглашение:
    search_agreement = selenium.find_element(By.CSS_SELECTOR, 'a.rt-link.rt-link--orange')
    time.sleep(5)
    # Находим Значки входа через соцсети (Вконтакте, Одноклассники, Mail.ru, Google, Яндекс).:
    search_button_vk = selenium.find_element(By.ID, 'oidc_vk')
    time.sleep(5)
    search_button_ok = selenium.find_element(By.ID, 'oidc_ok')
    time.sleep(5)
    search_button_mail = selenium.find_element(By.ID, 'oidc_mail')
    time.sleep(5)
    search_button_google = selenium.find_element(By.ID, 'oidc_google')
    time.sleep(5)
    search_button_ya = selenium.find_element(By.ID, 'oidc_ya')
    time.sleep(5)
    # Находим кнопку "Зарегистрироваться" по ID:
    search_button = selenium.find_element(By.ID, 'kc-register')
    # Находим Продуктовый слоган ЛК "Ростелеком ID":
    search_tagline = selenium.find_element(By.CSS_SELECTOR, 'p.what-is__desc')
    # Находим логотип Ростелекома:
    search_logo = selenium.find_element(By.CSS_SELECTOR, 'svg.rt-logo.what-is-container__logo')

    assert selenium.save_screenshot('test2.png')
