#encoding utf-8
import pytest
from Common.Read_yaml import Common_funcs

@pytest.fixture(scope="module")
def prefix():
    print("开始计算")
    yield
    print("\n结束计算")
CF=Common_funcs()
@pytest.fixture(params=CF.get_datas("\\datas\\datas.yml")[0],ids=CF.get_datas("\\datas\\datas.yml")[1])
def getAddDatas(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n结束计算")

@pytest.fixture(params=CF.get_datas("\\datas\\datas.yml")[6],ids=CF.get_datas("\\datas\\datas.yml")[7])
def getSubDatas(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n结束计算")

@pytest.fixture(params=CF.get_datas("\\datas\\datas.yml")[2],ids=CF.get_datas("\\datas\\datas.yml")[3])
def getDivDatas(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n结束计算")

@pytest.fixture(params=CF.get_datas("\\datas\\datas.yml")[4],ids=CF.get_datas("\\datas\\datas.yml")[5])
def getMulDatas(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n结束计算")
