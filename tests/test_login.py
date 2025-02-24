# import pytest
# from pages.login_page import LoginPage


# def test_login(driver):
#     # Инициализация
#     login_page = LoginPage(driver)
    
#     # Подготовка данных
#     test_data = generate_test_data()
    
#     # Выполнение действий
#     login_page.enter_email(test_data["email"])
    
#     # Проверка результатов
#     assert login_page.is_success_message_displayed()

    

# def test_login_positive(driver):
#     # Arrange (Подготовка)
#     login_page = LoginPage(driver)
#     test_user = {"email": "test@test.com", "password": "password123"}
    
#     # Act (Действие)
#     login_page.login(test_user["email"], test_user["password"])
    
#     # Assert (Проверка)
#     assert login_page.is_user_logged_in()