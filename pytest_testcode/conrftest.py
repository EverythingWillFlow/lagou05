import pytest
import yaml

from test_calculator import Calculator
import os

yaml_file_path = os.path.dirname(__file__) + "/test_data.yml"

with open(yaml_file_path) as f:
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

@pytest.fixture(params=add_datas, ids=add_ids)
def get_adds(request):
    print("\n开始计算")
    data = request.param
    print(f"request.param 的测试数据是：{data}")
    yield data
    print("\n结束计算")

@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_subs(request):
    print("\n开始计算")
    data = request.param
    print(f"request.param 的测试数据是：{data}")
    yield data
    print("\n结束计算")

@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_muls(request):
    print("\n开始计算")
    data = request.param
    print(f"request.param 的测试数据是：{data}")
    yield data
    print("\n结束计算")

@pytest.fixture(params=div_datas, ids=div_ids)
def get_divs(request):
    print("\n开始计算")
    data = request.param
    print(f"request.param 的测试数据是：{data}")
    yield data
    print("\n结束计算")

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc