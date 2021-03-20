from selenium.webdriver.common.by import By


class LoginPage:
    textbox_Email_id = (By.id, "Email")
    textbox_Password_id = (By.id, "Password")
    button_Submit_css = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def getEmail(self):
        self.driver.find_element(*LoginPage.textbox_Email_id).clear()
        return self.driver.find_element(*LoginPage.textbox_Email_id)

    def getPassword(self):
        self.driver.find_element(*LoginPage.textbox_Password_id).clear()
        return self.driver.find_element(*LoginPage.textbox_Password_id)

    def getLogin(self):
        self.driver.find_element(*LoginPage.button_Submit_css)
        return self.driver.find_element(*LoginPage.button_Submit_css)
