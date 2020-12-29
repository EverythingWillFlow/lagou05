import pytest
import yaml

from test_calculator import Calculator


def get_datas():
    with open("data.yml") as f:
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

def setup_module():
    print("\n整个test_calc.py模块开始前只执行一次")
def teardown_module():
    print("\n整个test_calc.py模块结束后只执行一次")


class TestCalc:

    def setup_class(self):
        self.calc = Calculator()
        print("\n所有用例执行前")
    def teardown_class(self):
        print("\n所有用例结束执行")

    def setup_methond(self):
        print("每个用例开始执行计算之前打印")
    def teardown_method(self):
        print("每个用例开始计算之后打印")

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