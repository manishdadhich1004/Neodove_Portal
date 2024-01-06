from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pageObjects.homePage import HomePage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    checkBox = (By.XPATH, "//span[@class='mat-checkbox-inner-container']")
    submit = (By.CSS_SELECTOR, "button[type='submit']")
    alreadyLogin = (By.CSS_SELECTOR, "button[class*='mat-focus-indicator confirm-btn-active']")

    def getUserName(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getCheckBox(self):
        return self.driver.find_element(*LoginPage.checkBox)

    def getSubmit(self):
        self.driver.find_element(*LoginPage.submit).click()
        homepage = HomePage(self.driver)
        return homepage

    def comfirmButtonVisible(self):
        return self.driver.find_element(*LoginPage.alreadyLogin)

    def login(self, username, password):
        self.getUserName().send_keys(username)
        self.getPassword().send_keys(password)
        self.getCheckBox().click()
        self.getSubmit()
        sleep(1)

        try:
            confirm_button = self.comfirmButtonVisible()

            if confirm_button.is_displayed():
                print("Confirm button is visible!")
                confirm_button.click()
            else:
                print("Confirm button is not visible.")

        except NoSuchElementException:
            print("Confirm button not found. User may not be logged in.")
        homepage = HomePage(self.driver)
        return homepage


