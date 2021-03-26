import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.Search import SearchCustomer
from Testdata.LoginUserData import LoginUserData
from Testdata.SearchCustomerData import SearchCustomerData
from Utils.BaseFile import BaseClass


class TestSearchCustomers(BaseClass):
    @pytest.mark.search
    def test_search_customer_by_email(self, search_customer):
        log = self.get_Logger("../Logs/search_customer.log")
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        search = SearchCustomer(self.driver)
        search.search_by_email(search_customer["email"])
        search.click_on_search()
        self.driver.execute_script("window.scrollBy(0,800)")
        searchlist = search.get_search_list()

        assert self.verify_customer(searchlist, search_customer["email"], log) == True
        log.info("*******************Test Case Passed**********")

    @pytest.fixture(params=SearchCustomerData.customer_record)
    def search_customer(self, request):
        return request.param
