from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Practice.config import details

class visbility_element(ec.visibility_of_element_located):
    def __call__(self, driver):
        ele = super().__call__(driver)
        if isinstance(ele,bool):
            return False
        else:
           is_enable = ele.is_enabled()
           return is_enable

def wait(func2):
    def wrapper(*args,**kwargs):
        instance , locator = args
        print(locator)
        w = WebDriverWait(instance.driver,details.timeout)
        v = visbility_element(locator)
        w.until(v)
        return func2(*args,**kwargs)
    return wrapper