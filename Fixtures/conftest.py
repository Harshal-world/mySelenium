from pytest import fixture, mark
from selenium import webdriver
# url = "https://demo.actitime.com/login.do"
url = "http://demowebshop.tricentis.com/"
@fixture
def init():
    driver = webdriver.Chrome(executable_path=r"C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe")
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

