import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.config.appConfig import AppConfig


@pytest.fixture(scope="class")
def setup(request):

    # Invoke Chrome
    service_obj = Service("../chromedriver-win64/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=service_obj)
    #driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(4)
    print(AppConfig.env)
    print(AppConfig.BASE_URL)
    driver.get(AppConfig.BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
