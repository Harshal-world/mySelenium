from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe")

#2 print the link text in python.org if 'Python is present'
# word ='Python'
# driver.get('https://www.python.org/')
# driver.maximize_window()
# ele1 = driver.find_element_by_xpath('//a[@title="The Python Programming Language"]')
# if word in ele1.text:
#     print(ele1.text)
#     print(ele1.get_attribute('href'))
#
# ele2 = driver.find_element_by_xpath('//a[@title="The Python Software Foundation"]')
# if word in ele2.text:
#     print(ele2.text)
#     print(ele2.get_attribute('href'))
#
# ele3 = driver.find_element_by_xpath('//a[@title="Python Documentation"]')
# if word in ele3.text:
#     print(ele3.text)
#     print(ele3.get_attribute('href'))
#
# ele4 = driver.find_element_by_xpath('//a[@title="Python Package Index"]')
# if word in ele4.text:
#     print(ele4.text)
#     print(ele4.get_attribute('href'))
#
# ele5 = driver.find_element_by_xpath('//a[@title="Python Job Board"]')
# if word in ele5.text:
#     print(ele5.text)
#     print(ele5.get_attribute('href'))
#
# ele6 = driver.find_element_by_xpath('//a[@class="current_item selectedcurrent_branch selected"]')
# if word in ele6.text:
#     print(ele6.text)
#     print(ele6.get_attribute('href'))




# #3. lin=k text of all the links in spide .com
# driver.get("https://www.spider.com/")
#
# ele = driver.find_element_by_link_text("Pricing")
# print(ele.text)
#
# ele2 = driver.find_element_by_link_text("Login")
# print(ele2.text)
#
# ele3 = driver.find_element_by_link_text("Sign Up")
# print(ele3.text)
#
# ele4 = driver.find_element_by_link_text("Start 14-Day Free Trial")
# print(ele4.text)
#
# ele5 = driver.find_element_by_link_text("")

#4. print title of all images in demowebshop if contains word computer
# word = 'computer'
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# ele1 = driver.find_element_by_xpath('//img[@src="/Themes/DefaultClean/Content/images/logo.png"]')
# if word in ele1.get_attribute('title'):
#     print(ele1.get_attribute('title'))
#
# ele2 = driver.find_element_by_xpath('//img[@src="http://demowebshop.tricentis.com/content/images/thumbs/0000015_25-virtual-gift-card_125.jpeg"]')
# # print(ele2.get_attribute('title'))
# if word in ele2.get_attribute('title'):
#     print(ele2.get_attribute('title'))
#
# ele3 = driver.find_element_by_xpath('//img[@src="http://demowebshop.tricentis.com/content/images/thumbs/0000224_141-inch-laptop_125.png"]')
# # print(ele3.get_attribute('title'))
# if word in ele3.get_attribute('title'):
#     print(ele3.get_attribute('title'))
#
# ele4 = driver.find_element_by_xpath('//a[@title="Show details for Build your own cheap computer"]')
# if word in ele4.get_attribute('title'):
#     print(ele4.get_attribute('title'))
# driver.quit()

#5. link text and href atrribute of yahoo.com
# driver.get("https://in.yahoo.com/?p=us&guccounter=1")
# driver.maximize_window()
# ele1 = driver.find_element_by_link_text('Sign in')
# print(ele1.text)
# print(ele1.get_attribute('href'))
#
# ele2 = driver.find_element_by_xpath('//a[@Class="_yb_1c1o9"]')
# print(ele2.text)
# print(ele2.get_attribute('href'))
#
# ele3 = driver.find_element_by_xpath('//a[@class="_yb_197nc "]')
# print(ele3.text)
# print(ele3.get_attribute('href'))
#
# ele4 = driver.find_element_by_xpath('(//a[@class="_yb_197nc "])[2]')
# print(ele4.text)
# print(ele4.get_attribute('href'))
#
# ele5 = driver.find_element_by_xpath('(//a[@class="_yb_197nc "])[3]')
# print(ele5.text)
# print(ele5.get_attribute('href'))
#
# ele6 = driver.find_element_by_xpath('(//a[@class="_yb_197nc "])[4]')
# print(ele6.text)
# print(ele6.get_attribute('href'))
#
# ele7 = driver.find_element_by_xpath('(//a[@class="_yb_197nc "])[5]')
# print(ele7.text)
# print(ele7.get_attribute('href'))
#
# ele8 = driver.find_element_by_xpath('(//a[@class="_yb_197nc "])[6]')
# print(ele8.text)
# print(ele8.get_attribute('href'))
#
# ele9 = driver.find_element_by_xpath('(//a[@class="_yb_197nc "])[7]')
# print(ele9.text)
# print(ele9.get_attribute('href'))
#
# ele10 = driver.find_element_by_xpath('(//a[@class="_yb_197nc "])[8]')
# print(ele10.text)
# print(ele10.get_attribute('href'))
#
# driver.quit()

