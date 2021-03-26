from selenium.webdriver.common.by import By


class SearchCustomer:
    textbox_email_id = (By.ID, "SearchEmail")
    textbox_Fname_id = (By.ID, "SearchFirstName")
    textbox_Lname_id = (By.ID, "SearchLastName")
    button_search_id = (By.ID, "search-customers")
    table_searchList_xpath = (By.XPATH, "//tr[@class='odd']/td[2]")

    def __init__(self, driver):
        self.driver = driver

    def search_by_email(self, email):
        self.driver.find_element(*SearchCustomer.textbox_email_id).send_keys(email)

    def search_by_First_Name(self, f_name):
        self.driver.find_element(*SearchCustomer.textbox_Fname_id).send_keys(f_name)

    def search_by_Last_Name(self, l_name):
        self.driver.find_element(*SearchCustomer.textbox_Lname_id).send_keys(l_name)

    def click_on_search(self):
        self.driver.find_element(*SearchCustomer.button_search_id).click()

    def get_search_list(self):
        return self.driver.find_elements(*SearchCustomer.table_searchList_xpath)

