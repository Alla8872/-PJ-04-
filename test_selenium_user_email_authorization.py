import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

def test_user_email_authorization(selenium):
    """ Авторизация пользователя по e-mail и паролю"""

    # Откроем сайт Ростелеком:
    selenium.get('https://b2c.passport.rt.ru/')
    time.sleep(5)
    # Находим поле ввода "Мобильный телефон":
    search_input_username = selenium.find_element(By.ID, 'username')
    search_input_username.clear()
    search_input_username.send_keys("allapod88@gmail.com")
    time.sleep(5)
    # Находим поле ввода "Пароль":
    search_input_password = selenium.find_element(By.ID, 'password')
    search_input_password.clear()
    search_input_password.send_keys("123123qwedsA111")
    time.sleep(5)
    # Находим кнопку "Войти" и нажимаем ее:
    search_button_login = selenium.find_element(By.ID, 'kc-login')
    search_button_login.submit()

    assert selenium.save_screenshot('test4.png')
