# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/cache.html) for more information.

##[第二次作业]()
- 补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
- 创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
- 将 fixture 方法存放在 conftest.py ，设置 scope=module
- 控制测试用例顺序按照【加-减-乘-除】这个顺序执行
- 结合 allure 生成本地测试报告