import pytest

from pythonCode.calculator import Calculator


class TestCalc:
    # 如下，当每个方法类都需要实例化Calculator时，将其抽取出来放到setup中
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()  # 实例化类,但是因为是在方类的，其他方法无法直接调用，所以前面加一个self,调用的时候也加上self.

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2], [1, 0, 1], [a, b, ab]],
                             ids=['int case', 'binum_case', 'float_case', 'minus_case', 'zero_case']
                             )
    def test_add(self, a, b, expect):
        # calc = Calculator()   #实例化类
        result = self.calc.add(a, b)  # 需要在calc前面加上self. 才能调用到setup里实例化的Calculator()类
        assert result == expect

    # 处理加法中浮点数精度不准确问题。python 浮点数（小数）在计算机中实际是以二进制存储的，并不精确。
    # 比如0.1是十进制，转换为二进制后就是一个无限循环的数，计算浮点数的时候难免产生误差， 这种情况可以使用decial库来提升精度，也可以使用round() 函数四舍五入进行运算。
    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [1, 0, 1]]
                             )
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b', [
        [0.1, 0], [10, 0]]
                             )
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    # # # 处理除数为0的情况 ，pytest.raises(ZeroDivisionError)此处只能捕获ZeroDivisionError(除数为0的情况)，如果除数非0，则会抛错
    # # def test_div_zero(self):
    #     with pytest.raises(ZeroDivisionError):
    #         result = self.cacl.div(1, 0)

    # #捕获异常
    # try:
    #     result = self.cacl.div(1, 0)
    # except ZeroDivisionError :
    #     print("除数为0")

# #用for循环实现上述用例
# def test_add1(self):
#     test_data = [
#     [1,1,2],[100,100,200],[0.1,0.1,0.2],[-1,-1,-2],[1,0,1] ]
#     for i in range(0,len(test_data)):
#         result = self.calc.add(test_data[i][0],test_data[i][1])
#         assert result == test_data[i][2]


# def test_add1(self):
#     #calc = Calculator()   #实例化类
#     result = self.calc.add(100,100)
#     assert result == 200
#
# def test_add2(self):
#     #calc = Calculator()   #实例化类
#     result = self.calc.add(0.1,0.1)
#     assert result == 0.2
#
