from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe')

# 1. Write a script to launch custom HTML page and click on "Business" link present inside a frame (switch to
# the frame using Name attribute)
driver.get(r'C:\Users\harsh\Desktop\mySelenium\iframe html.html')
driver.maximize_window()
driver.switch_to.frame("frame1")
driver.find_element('xpath','//a[text()="No Thanks"]').click()
driver.find_element('xpath','//a[text()="BUSINESS"]').click()
driver.switch_to.default_content()
driver.switch_to.frame("frame2")
driver.find_element('xpath','//a[text()="MENU +"]').click()
driver.quit()