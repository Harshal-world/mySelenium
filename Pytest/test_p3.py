import time

import pytest
from selenium import webdriver

input = [('admin','manager')]

class Test_Actitime:

    @pytest.mark.parametrize("username, passd",input)
    def test_fun(self,username,passd):
        driver = webdriver.Chrome(executable_path=r'C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe')
        driver.get('https://demo.actitime.com/login.do')
        driver.find_element('id','username').send_keys(username)
        driver.find_element('name','pwd').send_keys(passd)
        driver.find_element('xpath',"//div[text()='Login ']").click()
        time.sleep(2)
        assert driver.current_url == 'https://demo.actitime.com/user/submit_tt.do' , "failed"

