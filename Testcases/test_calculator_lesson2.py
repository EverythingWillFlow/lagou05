from pythoncode.calculator import Calculator
from Common.Read_yaml import Common_funcs
from allure_pytest import plugin as allure_plugin

import yaml,sys,os,allure
sys.path.append("../..")
import pytest

class Test_calculator():
    @pytest.mark.run(order=1)
    def test_add(self,getAddDatas):
        result = Calculator().add(getAddDatas[0],getAddDatas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert result == getAddDatas[2]

    @pytest.mark.run(order=4)
    def test_div(self,getDivDatas):
        result = Calculator().div(getDivDatas[0],getDivDatas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert result == getDivDatas[2]

    @pytest.mark.run(order=3)
    def test_mul(self,getMulDatas):
        result = Calculator().mul(getMulDatas[0],getMulDatas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert result == getMulDatas[2]

    @allure.feature("减法")
    @pytest.mark.run(order=2)
    def test_sub(self,getSubDatas):
        result = Calculator().sub(getSubDatas[0],getSubDatas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert result == getSubDatas[2]

if __name__ == '__main__':
    # pytest.main(['test_caculator.py ','-vs'])

    pytest.main(['-s', '-v', 'test_caculator_lesson2.py', '--html=../results/report.html', '--alluredir', '../results'])
    # pytest.main(args=["-vs", "test_caculator_lesson2.py","--alluredir=results"], plugins=[allure_plugin])
    split = 'allure ' + 'generate ' + '../Report ' + '-o ' + '../Html ' + '--clean'  # 生成Html报告语句
    os.system(split)  # 执行Html生成语句
