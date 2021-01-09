import pytest

from Common.Read_yaml import Common_funcs
from pythoncode.calculator import Calculator
@pytest.mark.parametrize("a,b,expected",Common_funcs().get_datas("\\datas\\data_div.yml")[0], ids=Common_funcs().get_datas("\\datas\\data_div.yml")[1])
def test_div(a,b,expected,prefix):
    assert Calculator().div(a,b) == expected