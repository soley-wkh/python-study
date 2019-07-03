# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/3 10:43
    file   : 02-unittest使用.py
    
"""
# 断言 编写代码时，我们总是会做出一些假设，断言就是用于在代码中捕获这些假设，
# 可以将断言看作是异常处理的一种高级形式
# assert 代表断言，假设断言的条件为真，如果为假诱发AssertionError
# assert 断言的条件，错误的提升

# a = 0
# assert a,'a is false'
# print(a)
# 上面的代码类似下面的if语句
# a = 0
# if not a:
#     raise AssertionError('a is false')
# print(a)


# import unittest
#
#
# # unittest的使用方法
# class MyTest(unittest.TestCase):
#     """
#     继承编写测试的基础类
#     """
#
#     def setUp(self):
#         """
#         类似于类的init方法，在测试执行之初启动执行，通常用来做测试数据的准备
#         """
#
#     def test_add(self):
#         """
#         具体测试的方法，使用testcase编写具体的方法，函数名称必须以test开头
#         函数当中的内容通常是获取预期值，和运行结果值
#         然后对两个值进行断言
#         """
#
#     def tearDown(self):
#
#         """
#         类似类的del方法。用来回收测试的环境
#         """
#
#
# if __name__ == '__main__':
#     unittest.main()


# 举个栗子
import unittest


class MyTest(unittest.TestCase):
    """
    继承编写测试的基础类
    """

    def setUp(self):
        """
        类似于类的init方法，在测试执行之初启动执行，通常用来做测试数据的准备
        """
        self.a = 1  # 测试使用的参数1
        self.b = 2  # 测试使用的参数2
        self.result = 3  # 预期的结果

    def test_add(self):
        """
        具体测试的方法，使用testcase编写具体的方法，函数名称必须以test开头
        函数当中的内容通常是获取预期值，和运行结果值
        然后对两个值进行断言
        """
        run_result = self.a + self.b
        self.assertEqual(run_result, self.result, 'self.a+self.b不等于3')  # 断言两个值相等

    def tearDown(self):
        """
        类似类的del方法。用来回收测试的环境
        """


if __name__ == '__main__':
    unittest.main()
