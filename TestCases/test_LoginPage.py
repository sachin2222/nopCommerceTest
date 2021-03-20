import pytest

from PageObjects.LoginPage import LoginPage
from Testdata.LoginUserData import LoginUserData
from Utils.BaseFile import BaseClass


class TestLoginPage(BaseClass):

    def test_user_credentials(self):
        self.driver.get("https://admin-demo.nopcommerce.com/")
        login = LoginPage(self.driver)

    @pytest.fixture(params= LoginUserData.LoginCredentials)
    def loginData(request):
        return request.param
