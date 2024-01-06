from pageObjects.loginPage import LoginPage
from testData.loginDetail import LoginData
from utilities.baseClass import BaseClass

class TestLogin(BaseClass):

    def test_login_using_password(self):
        loginpage = LoginPage(self.driver)
        homePage = loginpage.login(username=LoginData.username, password=LoginData.password)
        assert homePage.getTitle() == "Unsaved Changes"





