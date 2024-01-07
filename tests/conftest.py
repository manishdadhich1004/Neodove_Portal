import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.config.appConfig import AppConfig
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
        chromeDriverPath = ChromeDriverManager().install()
        service_obj = Service(executable_path=chromeDriverPath)
        chromeOption = Options()
        chromeOption.add_argument("--start-maximized")
        chromeOption.add_argument("--headless")
        driver = webdriver.Chrome(service=service_obj, options=chromeOption)
    elif browser_name == 'firefox':
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        service_obj = Service('./geckodriver-v0.32.2-win32/geckodriver.exe')
        driver = webdriver.Firefox(service=service_obj, options=options)
    
    driver.implicitly_wait(4)
    driver.get(AppConfig.BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()
