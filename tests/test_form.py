def test_form_submission(driver):
    form_page = FormPage(driver)
    form_page.fill_name("Test Name")
    form_page.fill_password("password123")
    # другие действия...
    # assertions