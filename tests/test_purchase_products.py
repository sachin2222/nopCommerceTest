import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from PageObjects.TshirtPage import TshirtPageObjects
from Utils.BaseFile import BaseClass
from PageObjects.HomePage import HomepageObjects


class TestPurchase(BaseClass):

    def test_Navigate_Tshirt_Category(self):
        self.driver.get("https://www.myntra.com/")
        homepage = HomepageObjects(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(homepage.Men_link()).click()
        homepage.Tshirt_link().click()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')



    def test_tshirt_SIZE_filter_Select_L(self, Filter_Info):
        tshirtpage = TshirtPageObjects(self.driver)
        filters = tshirtpage.get_top_filters()
        for filter in filters:
            print(filter.text)
            if filter.text == Filter_Info[0]:
                filter.click()
                break

        checkbox_list = tshirtpage.checkBox_list()
        print(len(checkbox_list))

        for checkBox in checkbox_list:
            print(checkBox.get_attribute("value"))
            if checkBox.get_attribute("value") == Filter_Info[1]:
                checkBox.find_element_by_xpath(".//following-sibling::div").click()
                break

    @pytest.fixture(params=[("Size", "L"), ("Country of Origin", "India"), ("Bundles", "Bundles")])
    def Filter_Info(self, request):
        return request.param
