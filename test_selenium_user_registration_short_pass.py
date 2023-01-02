import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

#python -m pytest -v --driver Chrome --driver-path C:/driver/chromedriver_win32/chromedriver.exe

def test_user_registration_short_pass(selenium):
    """Регистрация пользователя по e-mail и паролю длиной менее 8 символов"""
    # Переходим на сайт Ростелеком:
    selenium.get("https://b2c.passport.rt.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Находим кнопку "Зарегистрироваться" по ID и нажимаем ее:
    search_button = selenium.find_element(By.ID, 'kc-register')
    search_button.click()

    # Находим Поле ввода имени:
    search_input_first_name = selenium.find_element(By.NAME, 'firstName')
    search_input_first_name.clear()
    search_input_first_name.send_keys("Алла")
    # Находим Поле ввода фамилии:
    search_input_last_name = selenium.find_element(By.NAME, 'lastName')
    search_input_last_name.clear()
    search_input_last_name.send_keys("Иванова")
    # Находим Поле выбора региона:
    search_region = selenium.find_element(By.XPATH, '//input[@autocomplete="new-password"]')
    search_region.click()
    search_region.send_keys("Москва")
    # Находим Поле ввода email или мобильного телефона:
    search_input_email = selenium.find_element(By.ID, 'address')
    search_input_email.clear()
    search_input_email.send_keys("86alena86@mail.ru")
    # Находим Поле ввода пароля:
    search_input_password = selenium.find_element(By.ID, 'password')
    search_input_password.clear()
    search_input_password.send_keys("qwertyQ")
    # Находим Поле ввода подтверждения пароля:
    search_input_password_confirm = selenium.find_element(By.ID, 'password-confirm')
    search_input_password_confirm.clear()
    search_input_password_confirm.send_keys("qwertyQ")
    time.sleep(10)
    # Отображается сообщение: «Длина пароля должна быть не менее 8 символов»:
    assert selenium.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Длина пароля должна быть не менее 8 символов'
    assert selenium.save_screenshot('test14.png')