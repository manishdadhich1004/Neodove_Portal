from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Set up Chrome WebDriver
service_obj = webdriver.ChromeService("../chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://app-s2.neodove.com/login")

# Login
driver.find_element(By.NAME, "username").send_keys("9024204345")
driver.find_element(By.NAME, "password").send_keys("12345")
driver.find_element(By.XPATH, "//span[@class='mat-checkbox-inner-container']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
sleep(4)
# Handle Confirm button if present
try:
    confirm_button = driver.find_element(By.CSS_SELECTOR, "button[class*='mat-focus-indicator confirm-btn-active']")

    if confirm_button.is_displayed():
        print("Confirm button is visible!")
        confirm_button.click()
    else:
        print("Confirm button is not visible.")

except NoSuchElementException:
    print("Confirm button not found. User may not be logged in.")

# Click on the Filter button
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[mattooltip='Filter']"))
).click()

# Wait for the filter options dropdown to be present
dropdown_options = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[role='menuitem']")))

print(len(dropdown_options))

if len(dropdown_options) > 1:
    dropdown_options[1].click()
else:
    print("Dropdown doesn't have enough options.")

# Rest of your code...
