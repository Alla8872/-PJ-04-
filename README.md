Для тестирования применялась техника тест-дизайна "Позитивное и негативное тестирование". 
Негативное - с целью проверки внештатных ситуаций, в том числе ошибок пользователей.
Позитивное - для проверки правильности выполнения вызываемых функций в соответствии с требованиями к тестируемому приложению.

1. Файл test_selenium_registration.py проверяет пользовательский интерфейс формы регистрации пользователя в соответствии с требованиями.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_registration.py
2. Файл test_selenium_authorization.py проверяет пользовательский интерфейс формы авторизации пользователя в соответствии с требованиями.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_authorization.py
3. Файл test_selenium_user_registration.py проверяет возможность регистрации нового пользователя в веб-приложении с корректными данными.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_registration.py
4. Файл test_selenium_user_phone_authorization.py проверяет возможность авторизации существующего пользователя в веб-приложении по телефону с корректными данными.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_phone_authorization.py
5. Файл test_selenium_user_email_authorization.py проверяет возможность авторизации существующего пользователя в веб-приложении по email с корректными данными.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_email_authorization.py
6. Файл test_selenium_invalid_user_phone_authorization.py проверяет невозможность авторизации пользователя с некорректным номером телефона
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_invalid_user_phone_authorization.py
7. Файл test_selenium_invalid_user_email_authorization.py проверяет невозможность авторизации пользователя с некорректным email
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_invalid_user_email_authorization.py
8. Файл test_selenium_user_registration_exist_email.py проверяет невозможность регистрации нового пользователя под привязанным к УЗ email.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_registration_exist_email.py
9. Файл test_selenium_user_registration_exist_phone.py проверяет невозможность регистрации нового пользователя под привязанным к УЗ номером телефона.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_registration_exist_phone.py
10. Файл test_selenium_user_login_authorization.py проверяет возможность авторизации существующего пользователя в веб-приложении по логину с корректными данными.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_login_authorization.py
11. Файл test_selenium_invalid_user_login_authorization.py проверяет невозможность авторизации существующего пользователя в веб-приложении по некорректному логину.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_invalid_user_login_authorization.py
12. Файл test_selenium_reset_password_form.py проверяет пользовательский интерфейс формы восстановления пароля.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_reset_password_form.py
13. Файл test_selenium_empty_user_phone_authorization.py проверяет невозможность авторизации существующего пользователя в веб-приложении с пустым номером телефона.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_empty_user_phone_authorization.py
14. Файл test_selenium_user_registration_short_pass.py проверяет невозможность регистрации нового пользователя в веб-приложении с паролем длиной, короче 8 символов.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_registration_short_pass.py
15. Файл test_selenium_user_registration_lower_pass.py проверяет невозможность регистрации нового пользователя в веб-приложении с паролем в нижнем регистре.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_registration_lower_pass.py
16. Файл test_selenium_user_registration_cyrillic_pass.py проверяет невозможность регистрации нового пользователя в веб-приложении с паролем, прописанным кириллицей.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_registration_cyrillic_pass.py
17. Файл test_selenium_user_registration_diferent_pass.py проверяет невозможность регистрации существующего пользователя в веб-приложении с паролем, отличным от пароля-подтверждения.
Для запуска теста необходимо выполнить команду:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver.exe test_selenium_user_registration_diferent_pass.py
