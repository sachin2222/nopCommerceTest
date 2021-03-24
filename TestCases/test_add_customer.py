import pytest

from PageObjects.AddCustomer import AddCustomer
from PageObjects.LoginPage import LoginPage
from Testdata.LoginUserData import LoginUserData
from Testdata.addCustomerdata import addCustomerData

from Utils.BaseFile import BaseClass


class TestAddCustomer(BaseClass):

    def test_valid_user_credentials(self, valid_login_Data):
        log = self.get_Logger("../Logs/loginUser.log")
        log.info("Navigated to the Base URL:" + self.driver.current_url)
        login = LoginPage(self.driver)
        login.setEmail(valid_login_Data["email"])
        log.info("user has entered email: " + valid_login_Data["email"])

        login.setPassword(valid_login_Data["password"])
        log.info("user has entered password: " + valid_login_Data["password"])

        login.click_on_submit()
        log.info("User Clicks On Submit Button")
        dashboard_url = "https://admin-demo.nopcommerce.com/admin/"

        assert dashboard_url == self.driver.current_url
        log.info("*************Login ! Successful**************")
        log.info("*******************Test Case Passed**********")

    @pytest.fixture(params=LoginUserData.ValidLoginCredentials)
    def valid_login_Data(self, request):
        return request.param

    def test_add_customer(self, add_customer_data):
        log = self.get_Logger("../Logs/addcustomer.log")
        url = "https://admin-demo.nopcommerce.com/Admin/Customer/List"
        self.driver.get(url)
        log.info("Navigated to the Add Customer URL:" + url)
        ac = AddCustomer(self.driver)
        ac.click_on_addCustomer()
        ac.enter_email_address(add_customer_data["Email"])
        ac.enter_password(add_customer_data["Password"])
        ac.enter_first_name(add_customer_data["Firstname"])
        ac.enter_last_name(add_customer_data["Lastname"])
        ac.select_female()
        ac.select_dob(add_customer_data["DOB"])
        ac.select_tax_exempt_checkbox(True)
        ac.click_on_Cusrtomer_role()
        customer_roles_list = ac.get_customeRoles()
        self.click_element_by_getText(customer_roles_list, add_customer_data["customer_role"], log)
        ac.click_on_save_button()
        msg = ac.get_message_on_save()
        assert "successfully" in msg

    @pytest.fixture(params=addCustomerData.Customer_data)
    def add_customer_data(self, request):
        return request.param
