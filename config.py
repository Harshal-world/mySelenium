

from selenium import webdriver
driver = webdriver.Chrome(executable_path = r"C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe")

actual_url = "https://www.google.com/"
driver.get(actual_url)

driver.maximize_window()

current_url = driver.current_url

if actual_url in current_url:
    print("pass")

else:
    print("fail")



driver.close()

