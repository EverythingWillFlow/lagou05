#encoding utf-8
import pytest
@pytest.fixture(params=[1,2,3],ids=["test1","test2","test3"])
def prefix(request):
    print("获取数据")
    return request.param

def test_func1(prefix):
    print(f"这是test_func1，获取到的数据为{prefix}")