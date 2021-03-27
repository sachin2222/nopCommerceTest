import pytest

from PageObjects.Edit import EditCustomerDetails
from PageObjects.Search import SearchCustomer
from Testdata.SearchCustomerData import SearchCustomerData
from Utils.BaseFile import BaseClass


class Test_Edit_Customer(BaseClass):
    def test_edit_customer_details(self, edit_customer):
        log = self.get_Logger("../Logs/edit_customer.log")
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        log.info("****Navigated to the CustomerList URL****")
        search = SearchCustomer(self.driver)
        search.search_by_email(edit_customer["email"])
        search.click_on_search()
        self.driver.execute_script("window.scrollBy(0,800)")
        edit = EditCustomerDetails(self.driver)
        edit.click_on_Edit_button()
        edit.delete_customer()
        edit.confirm_delete()
        msg = edit.get_delete_message()
        assert "deleted successfully" in msg

    @pytest.fixture(params=SearchCustomerData.customer_record)
    def edit_customer(self, request):
        return request.param
