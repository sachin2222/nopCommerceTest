import time

import pytest
from selenium.webdriver import ActionChains

from Utils.BaseFile import BaseClass


class TestPurchase(BaseClass):
    def test_purchase_tshirt(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_link_text("Men"))
        self.driver.find_element_by_link_text("T-Shirts").click()
