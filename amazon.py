from selenium import webdriver
import re
driver = webdriver.Chrome(executable_path=r"C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.amazon.in/ref=ap_frn_logo")
driver.implicitly_wait(10)
driver.find_element('xpath', '(//span[text()="All"])[2]').click()
driver.find_element('link text', 'Mobiles, Computers').click()
driver.find_element('xpath',"//a[text()='Laptops']").click()
driver.execute_script("window.scrollTo(0,500)")
eles = driver.find_elements('xpath', "//div[@class='a-section a-spacing-none apb-browse-searchresults-product']")
l = []
for ele in eles:
    l.append(ele.text)

# print(l)
# print(l[0])
name,_, _, price, *rem = l[0].split('\n')

print(name)
print(re.sub(',','',price))
# driver.quit()