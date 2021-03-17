from selenium.webdriver.common.by import By


class TshirtPageObjects:

    sort_by = (By.XPATH, "//ul[@class='sort-list']/li/label/input")

    def __init__(self, driver):
        self.driver = driver

    def sort_list_values(self):
        return self.driver.find_elements(*TshirtPageObjects.sort_by)


