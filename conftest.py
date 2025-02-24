  # Конфигурация pytest и фикстуры
#   1. Основное назначение conftest.py:
# - Это специальный файл, который pytest автоматически обнаруживает
# - Используется для хранения общих фикстур и конфигураций
# - Фикстуры из этого файла доступны всем тестовым файлам без явного импорта
# - Позволяет переиспользовать код между разными тестовыми файлами
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from pages.form_page import FormPage  # Добавлен импорт

# Фикстура для создания и управления драйвером
@pytest.fixture
def driver():
     # Использование webdriver_manager для автоматического управления драйверами
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome()  # Создание драйвера
    driver.maximize_window()     # Максимизация окна
    yield driver                # Передача драйвера тестам
    driver.quit()              # Закрытие драйвера после тестов

@pytest.fixture
def form_page(driver):
    return FormPage(driver)

# Базовый класс для тестов
class BaseTest:
    pass

# Конфигурация для всех тестов
def pytest_configure(config):
    # Добавление пользовательских маркеров
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )

# Опционально: хук для обработки падающих тестов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            driver.save_screenshot(f"screenshot_{item.name}.png")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

