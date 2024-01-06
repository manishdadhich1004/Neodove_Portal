from time import sleep

from pageObjects.loginPage import LoginPage
from testData.loginDetail import LoginData
from utilities.baseClass import BaseClass
import pytest
from selenium.common.exceptions import NoSuchElementException


class TestLogin(BaseClass):

    def test_login_using_password(self):
        loginpage = LoginPage(self.driver)
        loginpage.getUserName().send_keys("9024204345")
        loginpage.getPassword().send_keys("12345")
        loginpage.getCheckBox().click()
        homePage = loginpage.getSubmit()
        # sleep(1)

        try:
            confirm_button = loginpage.comfirmButtonVisible()

            if confirm_button.is_displayed():
                print("Confirm button is visible!")
                confirm_button.click()
            else:
                print("Confirm button is not viisible.")

        except NoSuchElementException:
            print("Confirm button not found. User may not be logged in.")

        # sleep(1)
        assert homePage.getTitle() == "Unsaved Changes"





