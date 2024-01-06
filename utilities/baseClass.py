import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def giveExplicitWait(self, locator, duration):
        wait = WebDriverWait(self.driver, duration)
        wait.until(expected_conditions.presence_of_element_located(locator))


