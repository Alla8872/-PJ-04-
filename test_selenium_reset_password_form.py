import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

def test_reset_password_form(selenium):
    """ Форма восстановления пароля (UI)"""

    # Откроем сайт Ростелеком:
    selenium.get('https://b2c.passport.rt.ru/')
    time.sleep(5)

    # Находим Ссылку "Забыл пароль" и нажимаем ее:
    search_button_forgot_password = selenium.find_element(By.ID, 'forgot_password')
    search_button_forgot_password.click()
    # Находим заголовок "Восстановление пароля":
    assert selenium.find_element(By.CSS_SELECTOR, 'h1.card-container__title').text == "Восстановление пароля"
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
    # Находим поле ввода "Мобильный телефон":
    search_input_username = selenium.find_element(By.ID, 'username')
    # Находим поле ввода Капчи:
    search_kapcha = selenium.find_element(By.NAME, 'code')
    # Находим кнопку "Продолжить":
    search_kapcha = selenium.find_element(By.ID, 'reset')
    # Находим кнопку "Вернуться назад":
    search_reset_back = selenium.find_element(By.ID, 'reset-back')

    assert selenium.save_screenshot('test12.png')
