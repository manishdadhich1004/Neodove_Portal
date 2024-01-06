import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("../chromedriver-win64/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=service_obj)
    #driver = webdriver.Chrome(service=service_obj)
    driver.get("https://app-s2.neodove.com/login")
    driver.implicitly_wait(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
