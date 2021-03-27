from selenium.webdriver.common.by import By


class EditCustomerDetails:
    button_Edit_Xpath = (By.XPATH, "//a[contains(@href,'Edit')]")
    button_delete_ID = (By.ID, "customer-delete")
    button_confirm_delete_CSS = (By.CSS_SELECTOR, ".btn.btn-danger.float-right")
    message_delete_CSS = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissable")

    def __init__(self, driver):
        self.driver = driver

    def click_on_Edit_button(self):
        self.driver.find_element(*EditCustomerDetails.button_Edit_Xpath).click()

    def delete_customer(self):
        self.driver.find_element(*EditCustomerDetails.button_delete_ID).click()

    def confirm_delete(self):
        self.driver.find_element(*EditCustomerDetails.button_confirm_delete_CSS).click()

    def get_delete_message(self):
        return self.driver.find_element(*EditCustomerDetails.message_delete_CSS)
