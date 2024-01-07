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
    visibilityOff = (By.CSS_SELECTOR, "img.eye-close")
    visibilityOn = (By.CSS_SELECTOR, "img.eye")
    alreadyLogin = (By.XPATH, "//app-confirm-dialog/mat-dialog-actions/button/span[contains(text(), 'Continue')]")
    forgotPassword = (By.XPATH, "//span[text() = 'Forgot Password?']")
    signUpForAnAccount = (By.XPATH, "//span[text() = 'Sign up']")
    loginUsingOTP = (By.XPATH, "//div/b[text() = 'Log in using OTP']")

    def userNameField(self):
        return self.driver.find_element(*LoginPage.username)

    def passwordField(self):
        return self.driver.find_element(*LoginPage.password)

    def selectCheckBox(self):
        return self.driver.find_element(*LoginPage.checkBox)
    
    def visibilityOnButton(self):
        return self.driver.find_element(*self.visibilityOn)

    def visibilityOffButton(self):
        return self.driver.find_element(*self.visibilityOff)

    def submitButton(self):
        return self.driver.find_element(*LoginPage.submit)

    def comfirmButton(self):
        return self.driver.find_element(*LoginPage.alreadyLogin)

    def forgotPasswordButton(self):
        return self.driver.find_element(*LoginPage.forgotPassword)

    def signUpForAnAccountButton(self):
        return self.driver.find_element(*LoginPage.signUpForAnAccount)

    def loginUsingOtpButton(self):
        return self.driver.find_element(*LoginPage.loginUsingOTP)
        
    
    def validateLoginPage(self):
        self.driver.find_element(By.CSS_SELECTOR, "img[src='assets/images/login/hero.png']").is_displayed()
        self.driver.find_element(By.XPATH, "//div[text() = 'Log in']").is_displayed()
        self.userNameField().is_displayed()
        self.passwordField().is_displayed()
        self.selectCheckBox().is_displayed()
        assert 'I accept NeoDove Privacy Policy and Terms of Use' in self.driver.find_element(By.CSS_SELECTOR, 'span.mat-checkbox-label').text
        self.visibilityOffButton().is_displayed()
        self.forgotPasswordButton().is_displayed()
        self.signUpForAnAccountButton().is_displayed()
        self.loginUsingOtpButton().is_displayed()
    
    
    def login(self, username, password):
        self.userNameField().send_keys(username)
        self.passwordField().send_keys(password)
        self.selectCheckBox().click()
        self.submitButton().click()
        
        try:
            confirm_button = self.comfirmButton()
            sleep(2)
            if confirm_button.is_displayed():
                print("Confirm button is visible!")
                confirm_button.click()
            else:
                print("Confirm button is not visible.")

        except NoSuchElementException:
            print("Confirm button not found. User may not be logged in.")
        homepage = HomePage(self.driver)
        return homepage


