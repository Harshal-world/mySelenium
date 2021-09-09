
from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe")

# driver.get("https://demo.actitime.com/login.do")
# driver.maximize_window()
# driver.find_element_by_id("username").send_keys("admin")
# driver.find_element_by_name("pwd").send_keys("manager")

# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element_by_class_name("search-box-text.ui-autocomplete-input").send_keys("something")
# driver.find_element_by_class_name("button-1.search-box-button").click()
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element_by_css_selector('input[value="Search store"]').send_keys("computer")
# driver.find_element_by_css_selector('input[type="submit"]').click()


# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("//a[text() = 'Register']").click()
# driver.find_element_by_xpath('(//input[@name="Gender"])[1]').click()
# driver.find_element_by_xpath('//input[@id="FirstName"]').send_keys("demo")
# driver.find_element_by_xpath('//input[@id="LastName"]').send_keys("testing")
# driver.find_element_by_xpath('//input[@id="Email"]').send_keys("xyz@abc.in")
# driver.find_element_by_xpath('(//input[@type="submit"])[2]').click()

# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# driver.find_element_by_xpath('//input[@type="text"]').send_keys("onetwothree@fgh.com")
# driver.find_element_by_xpath('//input[@type="password"]').send_keys("12345678")
# driver.find_element_by_xpath('//button[@value="1"]').click()

# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("(//input[@name='pollanswers-1'])[1]").click()
# driver.find_element_by_xpath('//input[@value="Vote"]').click()

# driver.get("https://www.amazon.com/")
# driver.maximize_window()
# driver.find_element_by_xpath('//span[text()="Hello, Sign in"]').click()
# driver.find_element_by_name("email").send_keys("9579787164")
# driver.find_element_by_id("continue").click()
# driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_id("signInSubmit").click()

# from selenium.webdriver.support.select import Select
# driver.get("https://en-gb.facebook.com/")
# driver.maximize_window()
# driver.find_element_by_xpath('//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
# driver.find_element_by_name("firstname").send_keys("new account")
# driver.find_element_by_name("lastname").send_keys("hello")
# driver.find_element_by_name("reg_email__").send_keys("abc@123.in")
# driver.find_element_by_name("reg_passwd__").send_keys("123443231")
# day = driver.find_element_by_id("day")
# # day = driver.find_element_by_xpath('//select[@title="Day"]')
# s = Select(day)
# s.select_by_value("22")
#
# month = driver.find_element_by_id("month")
# s2 = Select(month)
# s2.select_by_visible_text("Dec")
#
# year = driver.find_element_by_id("year")
# s3= Select(year)
# s3.select_by_value("2000")


# import time
# from selenium.webdriver.support.select import Select
# from selenium.common.exceptions import StaleElementReferenceException
# driver.get("http://demowebshop.tricentis.com/books")
# driver.maximize_window()
# products = driver.find_element_by_id("products-orderby")
# s = Select(products)
#
# s.select_by_visible_text("Name: A to Z")
# time.sleep(2)
# try:
#     s.select_by_visible_text("Price: Low to High")
# except StaleElementReferenceException:
#     products = driver.find_element_by_id("products-orderby")
#     s = Select(products)
#     s.select_by_visible_text("Price: Low to High")

