import pytest
from test_param_yaml import get_datas
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("开始测试TestCalc")
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def teardown_class(self):
        print("TestCalc测试结束")

    def setup_method(self):
        print("\n计算开始")

    def teardown_method(self):
        print("\n计算结束")

    #  使用参数化
    # @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(10000,10000,20000)])
    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    # 测试add函数
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        print(str(a) + " + " + str(b) + " = " + str(result))
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', get_datas()[0])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        print(str(a) + " - " + str(b) + " = " + str(result))
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        print(str(a) + " * " + str(b) + " = " + str(result))
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', get_datas()[0])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        print(str(a) + " / " + str(b) + " = " + str(result))
        assert result == expect
