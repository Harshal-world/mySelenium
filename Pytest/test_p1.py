class TestFirst:

    def test_fun1(self):
        return 1 + 3

    def test_fun2(self):
        return  3 - 1

class TestSecond:

    def test_fun3(self):
        assert 1 + 3 > 5 , "wrong not matched"

    def test_fun4(self):
        assert 3 - 1  > 1, "matched"

    def test_fun5(self):
        assert 4 *0 < 0
