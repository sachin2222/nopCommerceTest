import pytest

from PageObjects.LoginPage import LoginPage
from Testdata.LoginUserData import LoginUserData
from Utils.BaseFile import BaseClass


class TestLoginPage(BaseClass):
    @pytest.mark.validuser
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

        login.click_on_logout()
        log.info("***********Logout! Successful*********************")
        url = "https://admin-demo.nopcommerce.com/"

        assert url in self.driver.current_url
        log.info("****************Test Case Passed**************")

    @pytest.mark.invaliduser
    def test_invalid_user_credentials(self, invalid_login_Data):
        log = self.get_Logger("../Logs/loginUser.log")
        log.info("Navigated to the Base URL:" + self.driver.current_url)

        login = LoginPage(self.driver)
        login.setEmail(invalid_login_Data["email"])
        log.info("user has entered email: " + invalid_login_Data["email"])

        login.setPassword(invalid_login_Data["password"])
        log.info("user has entered password: " + invalid_login_Data["password"])

        login.click_on_submit()
        log.info("User Clicks On Submit Button")

        error_msg = login.get_Error_Message()
        assert "Login was unsuccessful" in error_msg
        log.info("Login was Unsuccessful")

        log.info("*************Test Case Passed**************")

    @pytest.fixture(params=LoginUserData.ValidLoginCredentials)
    def valid_login_Data(self, request):
        return request.param

    @pytest.fixture(params=LoginUserData.InValidLoginCredential)
    def invalid_login_Data(self, request):
        return request.param
