from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe')

driver.maximize_window()

driver.get('https://www.bikedekho.com/bajaj-bikes')

driver.find_element("xpath","//span[text()='View Finance Offers']").click()
print("clicked")

driver.quit()