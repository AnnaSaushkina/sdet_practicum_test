 # Классы конкретных страниц
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# 2. FormPage - класс для работы конкретно с формой:
# - Содержит все локаторы элементов формы
# - Реализует специфические методы для работы с формой
# - Наследует базовые методы от BasePage
class FormPage(BasePage):
    NAME_FIELD = (By.ID, "name")
     # Заполнение поля имени
    def fill_name(self, name):
        self.input_text(self.NAME_FIELD, name)



    # PASSWORD_FIELD = (By.ID, "password")
    # DRINKS_CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox'][name='drinks']")
    # COLOR_DROPDOWN = (By.ID, "color")
    # AUTOMATION_RADIO = (By.CSS_SELECTOR, "input[type='radio'][name='automation']")
    # EMAIL_FIELD = (By.ID, "email")
    # TOOLS_COUNT_FIELD = (By.ID, "tools-count")
    # SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    # ALERT_MESSAGE = (By.CLASS_NAME, "alert")
    # - fill_name(): заполняет поле имени
    # - fill_password(): заполняет поле пароля
    # - select_drinks(): выбирает указанные напитки через чекбоксы
    # - select_color(): выбирает цвет из выпадающего списка
    # - select_automation_answer(): выбирает ответ про автоматизацию через радиокнопки
    # - fill_email(): заполняет поле email
    # - count_and_fill_tools(): считает количество инструментов и заполняет поле
    # - submit_form(): отправляет форму
    # - get_alert_text(): получает текст сообщения после отправки

    # def fill_password(self, password):
    #     """Заполнение поля пароля"""
    #     self.input_text(self.PASSWORD_FIELD, password)

    # def select_drinks(self, drinks):
    #     """
    #     Выбор напитков
    #     :param drinks: список напитков для выбора
    #     """
    #     drink_elements = self.find_elements(self.DRINKS_CHECKBOXES)
    #     for drink in drink_elements:
    #         if drink.get_attribute("value") in drinks:
    #             if not drink.is_selected():
    #                 drink.click()

    # def select_color(self, color):
    #     """Выбор цвета из выпадающего списка"""
    #     select = Select(self.find_element(self.COLOR_DROPDOWN))
    #     select.select_by_visible_text(color)

    # def select_automation_answer(self, answer):
    #     """Выбор ответа про автоматизацию"""
    #     radio_buttons = self.find_elements(self.AUTOMATION_RADIO)
    #     for radio in radio_buttons:
    #         if radio.get_attribute("value") == answer:
    #             radio.click()
    #             break

    # def fill_email(self, email):
    #     """Заполнение поля email"""
    #     self.input_text(self.EMAIL_FIELD, email)

    # def count_and_fill_tools(self):
    #     """Подсчет и заполнение количества инструментов"""
    #     tools = self.find_elements((By.CSS_SELECTOR, ".tool-item"))
    #     tools_count = len(tools)
    #     self.input_text(self.TOOLS_COUNT_FIELD, str(tools_count))

    # def submit_form(self):
    #     """Отправка формы"""
    #     self.click_element(self.SUBMIT_BUTTON)

    # def get_alert_text(self):
    #     """Получение текста алерта"""
    #     alert = self.find_element(self.ALERT_MESSAGE)
    #     return alert.text

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.url = "https://practice-automation.com/form-fields/"
        


    # def fill_name(self, name):
    #     name_field = self.wait.until(EC.presence_of_element_located(self.NAME_FIELD))
    #     name_field.send_keys(name)
        
    # def fill_password(self, password):
    #     # реализация
    #     pass


    # def setup(self, driver):
    #     self.form_page = FormPage(driver)
    #     self.form_page.open()

    # def test_complete_form_submission(self):
    #     """
    #     Проверка полного заполнения формы
    #     """
    #     self.form_page.fill_basic_info("Test User", "password123")
    #     self.form_page.select_drinks()
    #     self.form_page.select_color()
    #     self.form_page.fill_email("test@example.com")
        
    #     # Подсчет инструментов и добавление самого длинного
    #     tools_count = self.form_page.count_automation_tools()
    #     longest_tool = self.form_page.get_longest_tool_name()
    #     message = f"Tools count: {tools_count}\nLongest tool: {longest_tool}"
        
    #     self.form_page.fill_message(message)
    #     self.form_page.submit_form()
        
    #     # Проверка алерта
    #     assert self.form_page.get_alert_text() == "Message received!"
