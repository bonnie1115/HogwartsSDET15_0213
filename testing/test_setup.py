def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源销毁：teardown module")


def test_case1():
    print("test1")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")


class TestDemo:

    # 类级别的setup_class,teardown_class只在类的前后运行一次
    def setup_class(self):
        print("TestDemo setup_class 类级别")

    def teardown_class(self):
        print("TestDemo teardown_class 类级别")

    # 方法级别的setup_method==setup（在每个测试用例之前或后进行） 此处需要和unittest的区分开 unittest的是setUp
    def setup(self):
        print("TestDemo setup 方法级别")

    def teardown(self):
        print("TestDemo teardown 方法级别")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")


class TestDemo1:

    # 类级别的setup_class,teardown_class只在类的前后运行一次
    def setup_class(self):
        print("TestDemo setup_class 类级别")

    def teardown_class(self):
        print("TestDemo teardown_class 类级别")

    # 方法级别的setup_method==setup（在每个测试用例之前或后进行） 此处需要和unittest的区分开 unittest的是setUp
    def setup(self):
        print("TestDemo setup 方法级别")

    def teardown(self):
        print("TestDemo teardown 方法级别")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
