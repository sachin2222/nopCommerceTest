from selenium.webdriver.common.by import By


class LoginPage:
    textbox_Email_id = (By.ID, "Email")
    textbox_Password_id = (By.ID, "Password")
    button_Submit_css = (By.CSS_SELECTOR, "button[type='submit']")
    button_logout_linkText = (By.LINK_TEXT, "Logout")
    message_error_Class = (By.CSS_SELECTOR, ".message-error.validation-summary-errors")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(*LoginPage.textbox_Email_id).clear()
        return self.driver.find_element(*LoginPage.textbox_Email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(*LoginPage.textbox_Password_id).clear()
        return self.driver.find_element(*LoginPage.textbox_Password_id).send_keys(password)

    def click_on_submit(self):
        self.driver.find_element(*LoginPage.button_Submit_css).click()

    def click_on_logout(self):
        self.driver.find_element(*LoginPage.button_logout_linkText).click()

    def get_Error_Message(self):
        return self.driver.find_element(*LoginPage.message_error_Class).text
