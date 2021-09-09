import xlrd
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe')
# enter a data in demowebshop register page

wb = xlrd.open_workbook('pythonsel.xlsx')

ws = wb.sheet_by_name('Sheet2')
rows = ws.get_rows()
header = next(rows)

driver.get('http://demowebshop.tricentis.com/register')
driver.maximize_window()
for row in rows:
    driver.find_element('id','FirstName').send_keys(row[0].value)
    driver.find_element('id','LastName').send_keys(row[1].value)
    driver.find_element('id','Email').send_keys(row[2].value)