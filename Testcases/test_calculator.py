from pythoncode.calculator import Calculator
from Common.Read_yaml import Common
import pytest
import yaml,sys,os
sys.path.append("../..")

# @pytest.mark.parametrize("参数名",列表数据)
# 参数名：作为测试用例的参数. 字符串格式，多个参数中间用逗号隔开。
# 列表数据：一组测试数据。list格式，多组数据用元组类型，
# list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应。
# 可以添加ids参数指定用例说明(别名)。
#get_datas()[0]取返回列表[add_datas,add_ids]的第一个元素
import pytest
'''
* 模块级的（setup_module、teardown_module）全局的，在模块执行前运行一遍，在模块执行后运行一遍
* 函数级的（setup_function、teardown_function）只对函数用例生效，而且不在类中使用
* 类级的（setup_class、teardown_class）在类中使用，类执行之前运行一次，类执行之后运行一次
* 类中方法级的（setup_method、teardown_method）在每一个方法之前执行一次，在每一个方法之后执行一次
* 单独使用（setup、teardown）其作用和setup_function、teardown_function/setup_method、teardown_method 一样

'''

def setup_module():
    print("\nsetup_module:整个test_setup_teardown.py模块开始前只执行一次")
def teardown_module():
    print("\nteardown_module:整个test_setup_teardown.py模块结束后只执行一次")

def setup_function():
    print("\nsetup_function:不在类中的用例执行前")

def teardown_function():
    print("\nteardown_function:不在类中的用例执行后")

class Test_calculator():
    def setup_class(self):
        print("\nsetup_class:所有用例执行前")
    def teardown_class(self):
        print("\nteardown_class:所有用例结束执行")

    def setup_method(self):
        print("\nsetup_method:每个用例开始前执行")
    def teardown_method(self):
        print("\nteardown_method:每个用例结束执行")


    @pytest.mark.parametrize("a,b,expected",Common().get_datas("\\datas\\data_add.yml")[0], ids=Common().get_datas("\\datas\\data_add.yml")[1])
    def test_add(self,a,b,expected):
        assert Calculator().add(a,b) == expected

    @pytest.mark.parametrize("a,b,expected",Common().get_datas("\\datas\\data_sub.yml")[0], ids=Common().get_datas("\\datas\\data_sub.yml")[1])
    def test_sub(self,a,b,expected):
        assert Calculator().sub(a,b) == expected

    @pytest.mark.parametrize("a,b,expected",Common().get_datas("\\datas\\data_mul.yml")[0], ids=Common().get_datas("\\datas\\data_mul.yml")[1])
    def test_mul(self,a,b,expected):
        assert Calculator().mul(a,b) == expected
@pytest.mark.parametrize("a,b,expected",Common().get_datas("\\datas\\data_div.yml")[0], ids=Common().get_datas("\\datas\\data_div.yml")[1])
def test_div(a,b,expected):
    assert Calculator().div(a,b) == expected
