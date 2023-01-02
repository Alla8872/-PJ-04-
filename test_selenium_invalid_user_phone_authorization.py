import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

def test_invalid_user_phone_authorization(selenium):
    """ Авторизация пользователя по некорректному номеру телефона и корректному паролю"""

    # Откроем сайт Ростелеком:
    selenium.get('https://b2c.passport.rt.ru/')
    time.sleep(5)
    # Находим поле ввода "Мобильный телефон":
    search_input_username = selenium.find_element(By.ID, 'username')
    search_input_username.clear()
    search_input_username.send_keys("79123988826")
    time.sleep(5)
    # Находим поле ввода "Пароль":
    search_input_password = selenium.find_element(By.ID, 'password')
    search_input_password.clear()
    search_input_password.send_keys("123123qwedsA111")
    time.sleep(5)
    # Находим кнопку "Войти" и нажимаем ее:
    search_button_login = selenium.find_element(By.ID, 'kc-login')
    search_button_login.submit()

    assert selenium.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
    selenium.save_screenshot('test6.png')
