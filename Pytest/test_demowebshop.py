from selenium import webdriver
import xlrd
driver = webdriver.Chrome(executable_path=r'C:\Users\harsh\Desktop\mySelenium\Drivers\chromedriver.exe')
url = 'http://demowebshop.tricentis.com/register'
path = r'C:\Users\harsh\Desktop\mySelenium\Pytest\pythonsel.xlsx'
class TestDemoShopReg:
    def test_chromeCred(self,url):
        driver.get(url)
        driver.maximize_window()

    def test_cred(self, path):
        wb = xlrd.open_workbook(path)
        ws = wb.sheet_by_name('Sheet3')
        rows = ws.get_rows()
        header = next(rows)
        locators = {row[1].value: (row[0].value, row[2].value) for row in rows}
        # print(locators)
        for key, value in locators.items():
            ele = driver.find_element(value[0], key)
            if isinstance(value[1], str):
                ele.send_keys(value[1])
            else:
                ele.click()

obj = TestDemoShopReg()
obj.test_chromeCred(url)
obj.test_cred(path)










