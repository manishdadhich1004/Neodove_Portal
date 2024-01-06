from pageObjects.loginPage import LoginPage


class TestSMSAutomation:

    def test_sms_automation(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login("9024204345", "12345")

