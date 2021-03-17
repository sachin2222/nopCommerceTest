
from selenium.webdriver import ActionChains

from PageObjects.TshirtPage import TshirtPageObjects
from Utils.BaseFile import BaseClass
from PageObjects.HomePage import HomepageObjects


class TestPurchase(BaseClass):
    def test_purchase_tshirt(self):
        homepage = HomepageObjects(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(homepage.Men_link()).click()
        homepage.Tshirt_link().click()

        tshirtpage = TshirtPageObjects(self.driver)
        sort_list = tshirtpage.sort_list_values()
        print(len(sort_list))

        for value in sort_list:
            print(value.get_attribute("value"))
