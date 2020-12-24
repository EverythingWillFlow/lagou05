import pytest
import yaml
from pythoncode.test_calculator import Calculator

def get_datas():
    with open("calc_mark.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myids"]
        sub_datas = datas["subdatas"]
        sub_ids = datas["submyids"]
        mul_datas = datas["muldatas"]
        mul_ids = datas["mulmyids"]
        div_datas = datas["divdatas"]
        div_ids = datas["divmyids"]
        return [add_datas,add_ids,sub_datas,sub_ids,mul_datas,mul_ids,div_datas,div_ids]

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[2],ids=get_datas()[3])
    def test_sub(self,a,b,expect):
        result1 = self.calc.sub(a,b)
        assert result1 == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[4],ids=get_datas()[5])
    def test_mul(self,a,b,expect):
        result2 = self.calc.mul(a,b)
        assert result2 == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[6], ids=get_datas()[7])
    def test_div(self, a, b, expect):
        result3 = self.calc.div(a,b)
        assert result3 == expect