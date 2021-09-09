from selenium import webdriver
from Practice.config import *
from pytest import fixture
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--disable-notifications")

@fixture
def _driver():
    driver = webdriver.Chrome(details.chromePath,options=chromeoptions)
    driver.get(details.url)
    driver.maximize_window()
    yield driver
    driver.quit()

