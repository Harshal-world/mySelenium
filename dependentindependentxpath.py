import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe")
# Write a script to select the checkbox (in custom HTML page) corresponding to the languages mentioned in the list.
# driver.get(r"C:\Users\harsh\Desktop\mySelenium\Tables html.html")
# l = ["Ruby", "C#", "Java", "Python"]
# for item in l:
#     xpath_ = f'//td[text() = "{item}"]/..//input[@name="download"]'
#     driver.find_element_by_xpath(xpath_).click()

# Write a script to select different voting radio buttons in demo webshop page
# driver.get("http://demowebshop.tricentis.com/")
# l = ["Excellent", "Good", "Poor"]
# for item in l:
#     xpath_ = f'//label[text()="{item}"]/..//input[@name="pollanswers-1"]'
#     driver.find_element_by_xpath(xpath_).click()

# Exercise 4:
#
# Write a script to get the price tag of different gadgets in demo webshop and validate the actual price with pre-
# defined prices
#
# price_tag = {
# "$25 Virtual Gift Card": 25.00,
# '14.1-inch Laptop': 1590.00,
# 'Build your own cheap computer': 800.00,
# 'Simple Computer': 800.00,
# 'Build your own expensive computer': 1800.00,
# 'Build your own computer': 1200.00
# }
# driver.get("http://demowebshop.tricentis.com/")
# d ={}
# for key, values in price_tag.items():
#     _xpath = f'//span[text()="{values}"]/../../..//a[text()="{key}"]'
#     driver.find_element_by_xpath(_xpath)






# Write a script to add different books to the shopping cart and edit the quantities in the quantity text box
# _books = ['Fiction', 'Health Book']
#
# driver.get("http://demowebshop.tricentis.com/books")
# for item in _books:
#     xpath_ = f'//a[text()="{item}"]/../..//div[@class="buttons"]'
#     driver.find_element_by_xpath(xpath_).click()
#     time.sleep(2)
#
# _quantities = [4, 15]



# driver.get('http://demowebshop.tricentis.com/')
# driver.find_element_by_xpath('//a[text()="Facebook"]').click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.close()

# driver.find_element_by_id('email').send_keys('nothing')

# driver.get('https://www.naukri.com/')
# driver.maximize_window()
# handles = driver.window_handles
# for handle in handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     if driver.title == "Tech Mahindra":
#         driver.close()




# driver.get('http://demowebshop.tricentis.com/')
# driver.maximize_window()
# driver.find_element_by_xpath('//input[@value="Search"]').click()
# aobj = driver.switch_to.alert
# if aobj.text == "Please enter some search keyword":
#     print("pass")
# else:
#     print("fail")

# driver.get('https://www.naukri.com/')
# driver.maximize_window()
# handles = driver.window_handles
# for handle in handles[1:len(handles):1]:
#     driver.switch_to.window(handle)
#     driver.close()
#
# driver.switch_to.window(handles[0])
# path = r'C:\Users\harsh\Downloads\updated.pdf'
# driver.find_element_by_xpath('(//label[@class="btn"])[2]').send_keys(path)