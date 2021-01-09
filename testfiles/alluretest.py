import pytest
import requests
import allure
l = [
    {
        "url": "https://www.v2ex.com/api/site/info.json",
        "title":"v2ex的title",
        "desc":"v2ex的描述信息",
        "expect": {"title": "V2EX","slogan1111":"way to explore","domain":"www.v2ex.com"}
    },
    {
        "url": "https://cnodejs.org/api/vl/topics",
        "title":"cnodejs的title",
        "desc":"cnodejs的描述",
            "expect": {"success": True}},
]

@pytest.mark.parametrize("d", l)
def test_case(d):
    #allure的动态参数 dynamic
    allure.dynamic.title(d["title"])
    allure.dynamic.description(d["desc"])
    response = requests.get(url=d["url"]).json()
    for k in d["expect"]:
        print(333333,k)
        if d["expect"][k] != response.get(k,None):
            print(111111,"期望值",{k:d["expect"][k]},"实际值",{k:response.get(k,None)})
            assert d["expect"][k] == response.get(k,None)
    else:
        print(222222,"期望值",{k:d["expect"][k]},"实际值",{k:response.get(k,None)})
        assert d["expect"][k] == response.get(k,None)

@allure.title("登录用例")
def test_login():
    assert 1

@allure.title("注册用例")
@allure.description("注册用例的描述信息")
def test_register():
    assert 1

@allure.feature("登录功能")
class TestLogin(object):
    #Critical即影响系统功能或操作，主要功能存在严重缺陷，但不会影响到系统稳定性。比如说一个服务直接不可用了，微信不能发消息，支付宝不能付款这种，打开直接报错。
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录功能模块下的用例1")
    @allure.title("登录用例1")
    def test_login1(self):
        assert 1

    #Trivial轻微缺陷（必输项无提示，或者提示不规范），比如各种影响体验，但不影响使用的内容。
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("登录功能模块下的用例2")
    @allure.title("登录用例2")
    def test_login2(self):
        assert 0

@allure.feature("注册功能")
class TestRegister(object):
    #Major即界面、性能缺陷、兼容性。如操作界面错误（包括数据窗口内列名定义、含义是否一致）、长时间操作无进度提示等。
    @allure.severity(allure.severity_level.MINOR)
    @allure.story("注册功能模块下的用例1")
    @allure.title("注册用例1")
    def test_reg1(self):
        assert 1

    #BLOCKER中断缺陷（客户端程序无响应，无法执行下一步操作），系统无法执行、崩溃或严重资源不足、应用模块无法启动或异常退出、无法测试、造成系统不稳定。
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("注册功能模块下的用例2")
    @allure.title("注册用例2")
    def test_reg2(self):
        assert 1

if __name__ == '__main__':
    pytest.main(["-s","test_case.py"])