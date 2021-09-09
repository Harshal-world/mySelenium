class TestDemoWebShop:
    def test_login(self,init):
        init.find_element('xpath','//a[text()="Log in"]').click()
        init.find_element('id','Email').send_keys("asdfghj")
        init.find_element('id','Password').send_keys('123456')
        init.find_element('xpath',"//input[@value='Log in']").click()
        
