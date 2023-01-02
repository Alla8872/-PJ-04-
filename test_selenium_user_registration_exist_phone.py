import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/driver/chromedriver_win32/chromedriver.exe')

#python -m pytest -v --driver Chrome --driver-path C:/driver/chromedriver_win32/chromedriver.exe test_selenium_petfri

def test_user_registration(selenium):
    """Регистрация пользователя по номеру телефона, привязанному к имеющейся учетной записи"""
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
    search_input_email.send_keys("79123988827")
    # Находим Поле ввода пароля:
    search_input_password = selenium.find_element(By.ID, 'password')
    search_input_password.clear()
    search_input_password.send_keys("232323qwertyQ12")
    # Находим Поле ввода подтверждения пароля:
    search_input_password_confirm = selenium.find_element(By.ID, 'password-confirm')
    search_input_password_confirm.clear()
    search_input_password_confirm.send_keys("232323qwertyQ12")
    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    # Находим  Кнопку "Зарегистрироваться":
    search_button_register = selenium.find_element(By.NAME, 'register')
    search_button_register.submit()
    # Make the screenshot of browser window:
    assert selenium.find_element(By.CSS_SELECTOR, 'h2.card-modal__title').text == "Учётная запись уже существует"
    assert selenium.find_element(By.NAME, 'gotoLogin').text == "Войти"
    assert selenium.find_element(By.ID, 'reg-err-reset-pass').text == "Восстановить пароль"
    selenium.save_screenshot('test8.png')
