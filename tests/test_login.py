import time
from pageObjects.loginPage import LoginPage
from testData.loginDetail import LoginData
from utilities.baseClass import BaseClass
from selenium.webdriver.common.by import By

class TestLogin(BaseClass):

    def test_validate_login_page(self):
        loginpage = LoginPage(self.driver)
        self.reloadPage()
        loginpage.validateLoginPage()


    def test_login_using_password(self):
        loginpage = LoginPage(self.driver)
        homePage = loginpage.login(username=LoginData.username, password=LoginData.password)
        assert homePage.get_title() == "UTILITY MALL"





