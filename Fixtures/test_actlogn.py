from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestLogin:
    data = [('admin','manager'),('trainee','trainee'),('admin','trainee')]
    @mark.parametrize("id,passd",data)
    def test_login(self,id, passd,init):
        init.find_element('id','username').send_keys(id)
        init.find_element('name','pwd').send_keys(passd)
        init.find_element('xpath','//div[text()="Login "]').click()
        wait = WebDriverWait(init,timeout=30)
        wait.until(expected_conditions.url_matches("https://demo.actitime.com/user/submit_tt.do"))
        # init.implicitly_wait(10)

        assert init.current_url == 'https://demo.actitime.com/user/submit_tt.do',"failed to login"

    