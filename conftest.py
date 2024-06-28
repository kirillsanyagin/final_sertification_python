import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import chrome, firefox, microsoft
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="function")
def browser():
    if testdata["browser"] == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        yield driver
        driver.quit()
    elif testdata["browser"] == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
        yield driver
        driver.quit()
    elif testdata["browser"] == "microsoft":
        service = Service(executable_path=EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
        yield driver
        driver.quit()

@pytest.fixture()
def login():
    response = requests.post(testdata['website'],
                             data={'username': testdata['login'], 'password': testdata['password']})
    if response.status_code == 200:
        return response.json()['token']

@pytest.fixture()
def user_id():
    response = requests.post(testdata['website'],
                             data={'username': testdata['login'], 'password': testdata['password']})
    if response.status_code == 200:
        return response.json()['id']