# Базовый класс для всех страниц
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. BasePage - базовый класс, который содержит общие методы для работы с элементами:
# - Поиск элементов с ожиданием
# - Клики по элементам
# - Ввод текста
# - Обработка общих действий
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Поиск элемента с ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Поиск всех элементов с ожиданием"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """Клик по элементу с ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        """Ввод текста в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)