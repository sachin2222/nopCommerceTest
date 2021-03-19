import pytest
from selenium.webdriver import ActionChains
from PageObjects.TshirtPage import TshirtPageObjects
from Testdata.TshirtData import TshirtData
from Utils.BaseFile import BaseClass
from PageObjects.HomePage import HomepageObjects


class TestPurchase(BaseClass):

    def test_tshirt_X_filter_Select_Y(self, Filter_Info):
        log = self.get_Logger("t-shirt_purchase_functionality.log")
        self.driver.get("https://www.myntra.com/")

        log.info("Invoking Web Browser")
        homepage = HomepageObjects(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(homepage.Men_link()).perform()
        log.info("Move to Men Category")

        homepage.Tshirt_link().click()
        log.info("Click on Tshirt Link Under Men category")

        tshirtpage = TshirtPageObjects(self.driver)
        filters = tshirtpage.get_top_filters()
        log.info("Got all the top Filters")

        self.click_element_by_getText(filters, Filter_Info["Filter_Name"], log)
        log.info("Selected the Required Filter by name")

        checkbox_list = tshirtpage.checkBox_list()
        self.click_checkbox_by_getAtrribute(checkbox_list, Filter_Info["Filter_Value"], log)
        log.info("Selected the Required CheckBox Button to Filter")


    @pytest.fixture(
        params=TshirtData.tshirt_Filter_values)
    def Filter_Info(self, request):
        return request.param
