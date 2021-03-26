import pytest

from PageObjects.AddCustomer import AddCustomer
from Testdata.addCustomerdata import addCustomerData
from Utils.BaseFile import BaseClass


class TestAddCustomer(BaseClass):
    def test_add_customer(self, add_customer_data):
        log = self.get_Logger("../Logs/addcustomer.log")
        url = "https://admin-demo.nopcommerce.com/Admin/Customer/List"
        self.driver.get(url)
        log.info("Navigated to the Add Customer URL:" + url)
        ac = AddCustomer(self.driver)
        ac.click_on_addCustomer()
        log.info("Enter the Customer Details")

        ac.enter_email_address(add_customer_data["Email"])
        ac.enter_password(add_customer_data["Password"])
        ac.enter_first_name(add_customer_data["Firstname"])
        ac.enter_last_name(add_customer_data["Lastname"])
        ac.select_gender(add_customer_data["Gender"])
        ac.select_dob(add_customer_data["DOB"])
        ac.select_tax_exempt_checkbox(True)
        ac.click_on_Customer_role()
        customer_roles_list = ac.get_customerRoles()
        self.click_element_by_getText(customer_roles_list, add_customer_data["customer_role"], log)
        ac.click_on_save_button()
        msg = ac.get_message_on_save()
        log.info(msg)
        assert "successfully" in msg
        log.info("*******************Test Case Passed**********")

    @pytest.fixture(params=addCustomerData.Customer_data)
    def add_customer_data(self, request):
        return request.param
