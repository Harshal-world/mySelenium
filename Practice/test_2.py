from pytest import mark
from Practice.functions import *
data = [('admin','manager'),
        ('trainee','trainee')]
headers = "username, password"


@mark.parametrize(headers,data)
def test_two(username,password,_driver):
    f2 = func(_driver)
    f2.entertext(('id','username'),text=username)
    f2.entertext(('name','pwd'),text=password)
    f2.click(('xpath','//div[text()="Login "]'))
    # _driver.switch_to.alert.accept()
    f2.click(('id','logoutLink'))




