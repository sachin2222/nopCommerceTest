from selenium.webdriver.common.by import By


class AddCustomer:
    dropdown_customers_xpath = (By.XPATH, "//li[@class='nav-item has-treeview menu-open']/a")
    button_addCustomer_xpath = (By.XPATH, "//div[@class='float-right']/a")
    textbox_email_id = (By.ID, "Email")
    textbox_Password_id = (By.ID, "Password")
    textbox_Firstname_id = (By.ID, "FirstName")
    textbox_Lastname_id = (By.ID, "LastName")
    radiobutton_genderFemale_id = (By.ID, "Gender_Female")
    radiobutton_genderMale_id = (By.ID, "Gender_Male")
    textbox_DOB_id = (By.ID, "DateOfBirth")
    textbox_customerRole_CSS = (By.CSS_SELECTOR, ".k-item")
    textbox_cr_XPATH = (By.XPATH, "//input[@aria-labelledby='SelectedCustomerRoleIds_label']")
    checkbox_tax_ID = (By.ID, "IsTaxExempt")
    button_save_CSS = (By.CSS_SELECTOR, "button[name='save']")
    message_success_CSS = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissable")

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_label(self):
        self.driver.find_element(*AddCustomer.dropdown_customers_xpath).click()

    def click_on_addCustomer(self):
        self.driver.find_element(*AddCustomer.button_addCustomer_xpath).click()

    def enter_email_address(self, email):
        self.driver.find_element(*AddCustomer.textbox_email_id).send_keys(email)

    def enter_password(self, pwd):
        self.driver.find_element(*AddCustomer.textbox_Password_id).send_keys(pwd)

    def enter_first_name(self, f_name):
        self.driver.find_element(*AddCustomer.textbox_Firstname_id).send_keys(f_name)

    def enter_last_name(self, l_name):
        self.driver.find_element(*AddCustomer.textbox_Lastname_id).send_keys(l_name)

    def select_gender(self, gender):
        if gender == "M":
            self.driver.find_element(*AddCustomer.radiobutton_genderMale_id).click()
        if gender == "F":
            self.driver.find_element(*AddCustomer.radiobutton_genderFemale_id).click()


    def select_dob(self, dob):
        self.driver.find_element(*AddCustomer.textbox_DOB_id).send_keys(dob)

    def get_customerRoles(self):
        return self.driver.find_elements(*AddCustomer.textbox_customerRole_CSS)

    def click_on_Customer_role(self):
        self.driver.find_element(*AddCustomer.textbox_cr_XPATH).click()

    def select_tax_exempt_checkbox(self, flag):
        if flag == True:
            self.driver.find_element(*AddCustomer.checkbox_tax_ID).click()

    def click_on_save_button(self):
        self.driver.find_element(*AddCustomer.button_save_CSS).click()

    def get_message_on_save(self):
        return self.driver.find_element(*AddCustomer.message_success_CSS).text
