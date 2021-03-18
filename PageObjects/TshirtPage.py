from selenium.webdriver.common.by import By


class TshirtPageObjects:
    Top_Filters = (By.XPATH, "//ul[@class='atsa-filters']/li/label")
    checkboxes_label = (By.XPATH, "//label[@class='common-customCheckbox']/input")
    checkbox_button = (By.XPATH, ".//following-sibling::div")

    def __init__(self, driver):
        self.driver = driver

    def get_top_filters(self):
        return self.driver.find_elements(*TshirtPageObjects.Top_Filters)

    def checkBox_list(self):
        return self.driver.find_elements(*TshirtPageObjects.checkboxes_label)

    def click_on_checkbox(self):
        self.driver.find_element(*TshirtPageObjects.checkbox_button).click()
