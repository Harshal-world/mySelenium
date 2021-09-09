from Practice.functions import *
from pytest import mark

data = [('admin','manager'),
        ('trainee','trainee')]
headers = "username, password"

@mark.parametrize(headers,data)
def test_one(username,password,_driver):
    f = func(_driver)
    f.entertext(('id', 'username'), text = username)
    f.entertext(('name', 'pwd'), text = password)
    f.click(('xpath','//div[text()="Login "]'))
    f.click(('id','container_tasks'))
    f.click(('xpath','//div[text()="Add New"]'))
    f.click(('css selector','.item.createNewTasks'))
    f.click(('id', 'logoutLink'))




