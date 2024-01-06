import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.config.appConfig import AppConfig
from selenium.webdriver.firefox.options import Options

# used for taking input from browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="launch chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    # Invoke Chrome
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        service_obj = Service('../chromedriver-win64/chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == 'firefox':
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        service_obj = Service('./geckodriver-v0.32.2-win32/geckodriver.exe')
        driver = webdriver.Firefox(service=service_obj, options=options)


    #options = webdriver.ChromeOptions()
    #options.add_experimental_option("detach", True)
    #driver = webdriver.Chrome(options=options, service=service_obj)
    
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get(AppConfig.BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()
