from pages.form_page import FormPage

class TestFormPage:
    def test_basic_form_submission(self, driver):
        """
        Базовый позитивный тест-кейс:
        - Заполнение всех полей валидными данными
        - Проверка появления алерта
        """
        form_page = FormPage(driver)
        form_page.fill_name("John Doe")
        form_page.fill_password("secure123")
        form_page.select_drinks(["coffee", "tea"])
        form_page.select_color("Blue")
        form_page.select_automation_answer("yes")
        form_page.fill_email("john@example.com")
        form_page.count_and_fill_tools()
        form_page.submit_form()
        
        assert form_page.get_alert_text() == "Form submitted successfully!"

    # def test_multiple_drink_selection(self, driver):
    #     """
    #     Проверка множественного выбора напитков:
    #     - Выбор Milk и Coffee
    #     - Проверка, что оба значения выбраны
    #     """
    #     pass

    # def test_email_validation(self, driver):
    #     """
    #     Проверка валидации email:
    #     - Попытка ввода некорректного email
    #     - Попытка ввода корректного email
    #     """
    #     pass

    # def test_automation_tools_count(self, driver):
    #     """
    #     Проверка подсчета инструментов:
    #     - Подсчет количества инструментов
    #     - Ввод числа в поле Message
    #     """
    #     pass

    # def test_longest_tool_name(self, driver):
    #     """
    #     Дополнительный тест для определения самого длинного названия инструмента:
    #     - Поиск инструмента с максимальной длиной
    #     - Добавление его в поле Message
    #     """
    #     pass
