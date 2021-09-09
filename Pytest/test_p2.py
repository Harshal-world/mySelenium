import pytest
data = [1,2,3,4]
l = []
class Testpara:
    @pytest.mark.parametrize("a",data)
    def test_fun1(self,a):
         l.append(a)
         assert  l[a-1] == a, "failed"

    @pytest.mark.parametrize("b",data)
    def test_fun2(self,b):
        l.pop(b)

