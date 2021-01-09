import pytest
@pytest.fixture()
def prefix():
    print("开始计算")
    yield
    print("\n结束计算")