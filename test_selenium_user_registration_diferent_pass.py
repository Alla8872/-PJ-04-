import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

#python -m pytest -v --driver Chrome --driver-path C:/driver/chromedriver_win32/chromedriver.exe

def test_user_registration_diferent_pass(selenium):
    """Регистрация пользователя по e-mail и паролю  отличному от пароля-подтверждения"""
    # Переходим на сайт Ростелеком:
    selenium.get("https://b2c.passport.rt.ru/")

    time.sleep(5)

    # Находим кнопку "Зарегистрироваться" по ID и нажимаем ее:
    search_button = selenium.find_element(By.ID, 'kc-register')
    search_button.click()

    # Находим Поле ввода имени:
    search_input_first_name = selenium.find_element(By.NAME, 'firstName')
    search_input_first_name.clear()
    search_input_first_name.send_keys("Алла")
    time.sleep(5)
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
    search_input_password.send_keys("232323qwertyQ")
    # Находим Поле ввода подтверждения пароля:
    search_input_password_confirm = selenium.find_element(By.ID, 'password-confirm')
    search_input_password_confirm.clear()
    search_input_password_confirm.send_keys("232323qwertyQW")
    time.sleep(5)
    # Находим  Кнопку "Зарегистрироваться" и нажимаем ее:
    search_button_register = selenium.find_element(By.NAME, 'register')
    search_button_register.click()
    # Отображается сообщение: «Пароль должен содержать хотя бы одну заглавную букву»:
    assert selenium.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error').text == 'Пароли не совпадают'
    assert selenium.save_screenshot('test17.png')