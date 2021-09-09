from selenium import webdriver
opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications--")
driver = webdriver.Chrome(executable_path=r'C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe',options=opt)


# 1.Count number of images on the webpage
# driver.get('http://demowebshop.tricentis.com/')
# driver.maximize_window()
# images = driver.find_elements('xpath','//img')
#
# print(len(images))
# driver.get('http://demowebshop.tricentis.com/')
#
# images = driver.find_elements_by_xpath("//img")
#
# print('Total Images on the page: ',len(images))
# driver.quit()

# 2.Print the link text of all the links in python.org iff the linktext contains word 'Python' in it. Also, print the
# attribute 'href' of the corresponding link.
# driver.get('https://www.python.org/')
# driver.maximize_window()
# links = driver.find_elements('xpath','//a')
# for link in links:
#     if 'Python' in link.text:
#         print(link.text)
#         print(link.get_attribute('href'))
#
# driver.quit()

# 3.Print the link text of all the links in spiders.com iff the linktext contains word 'spiders' in it. Also, print the
# attribute 'href' of the corresponding link.
# driver.get('https://www.spider.com/')
# driver.maximize_window()
# links = driver.find_elements('xpath','//a')
# for link in links:
#     if 'Spiders' in link.text:
#         print(link.text)
#         print(link.get_attribute('href'))
#
# driver.quit()


# 4.Print the title of all the images in demowebsop iff the title contains word 'computer' in it.
# driver.get('http://demowebshop.tricentis.com/')
# driver.maximize_window()
# images = driver.find_elements('xpath','//img')
# for image in images:
#     if 'computer' in image.get_attribute('title'):
#         print(image.get_attribute('title'))
#
# driver.quit()

# 5.Write a script to print the link text and href attribute of all the links present on the header of yahoo.com
# driver.get('https://in.yahoo.com/?p=us')
# driver.maximize_window()
# elements = driver.find_elements('xpath','//div[@id="ybar-navigation"]//a')
# for element in elements:
#     print(element.text)
#     print(element.get_attribute('href'))
#
# driver.quit()


# driver.get('https://www.sharekhan.com/')
# driver.maximize_window()
# driver.quit()


###### flipcart login
# driver.get('https://www.flipkart.com/')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element('xpath',"(//input[@type='text'])[2]").send_keys("hello@gmail.com")
# driver.find_element('xpath',"//input[@type='password']").send_keys("hello@123")
# driver.find_element('xpath',"(//span[text()='Login'])[2]").click()
# driver.quit()