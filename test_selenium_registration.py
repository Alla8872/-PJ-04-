import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

def test_registration(selenium):
    """ Регистрация пользователя"""

    # Откроем сайт Ростелеком:
    selenium.get('https://b2c.passport.rt.ru/')

    # Находим заголовок "Авторизация" по имени класса:
    search_auth = selenium.find_element(By.CLASS_NAME, 'card-container__title')

    # Находим кнопку "Зарегистрироваться" по ID и нажимаем ее:
    search_button = selenium.find_element(By.ID, 'kc-register')
    search_button.click()
    # Находим Поле ввода имени:
    search_input_first_name = selenium.find_element(By.NAME, 'firstName')
    # Находим Поле ввода фамилии:
    search_input_last_name = selenium.find_element(By.NAME, 'lastName')
    # Находим Поле выбора региона:
    search_region = selenium.find_element(By.CLASS_NAME, 'rt-input__input.rt-input__input--rounded.rt-input__input--orange')
    # Находим Поле ввода email или мобильного телефона:
    search_input_email = selenium.find_element(By.ID, 'address')
    # Находим Поле ввода пароля:
    search_input_password = selenium.find_element(By.ID, 'password')
    # Находим Поле ввода подтверждения пароля:
    search_input_password_confirm = selenium.find_element(By.ID, 'password-confirm')
    # Находим  Кнопку "Зарегистрироваться":
    search_button_register = selenium.find_element(By.NAME, 'register')
    # Находим  Ссылки на пользовательское соглашение:
    search_agreement = selenium.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(5) > a')
    # Make the screenshot of browser window:
    assert selenium.save_screenshot('test1.png')
