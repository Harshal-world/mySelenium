from selenium.webdriver.support.select import Select
from Practice.decrts import *

class func():
    def __init__(self,driver):
        self.driver = driver
    @wait
    def click(self,locator):
        self.driver.find_element(*locator).click()


    @wait
    def entertext(self,locator, *,text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)


    @wait
    def selectopt(self,locator,*,text):
       ele =  self.driver.find_element(*locator)
       s = Select(ele)
       s.select_by_visible_text(text)