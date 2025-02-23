import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsite(unittest.TestCase):
    def setUp(self):
        # Инициализация драйвера перед каждым тестом
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def test_website_url(self):
        # Тест 1: Проверка URL
        self.driver.get("https://example.com")
        self.assertIn("example", self.driver.current_url, "URL не содержит 'example'!")
        
    def test_browser_launch(self):
        # Тест 2: Проверка запуска браузера
        try:
            self.driver.get("https://google.com")
            self.assertTrue(True, "Браузер успешно запущен")
        except Exception as e:
            self.fail(f"Ошибка при запуске браузера: {e}")
    
    def tearDown(self):
        # Закрытие браузера после каждого теста
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
