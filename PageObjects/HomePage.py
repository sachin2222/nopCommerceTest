from selenium.webdriver.common.by import By

from PageObjects.TshirtPage import TshirtPageObjects


class HomepageObjects:
    Men = (By.LINK_TEXT, "Men")
    Tshirt = (By.LINK_TEXT, "T-Shirts")

    def __init__(self, driver):
        self.driver = driver

    def Men_link(self):
        return self.driver.find_element(*HomepageObjects.Men)

    def Tshirt_link(self):
        return self.driver.find_element(*HomepageObjects.Tshirt)
