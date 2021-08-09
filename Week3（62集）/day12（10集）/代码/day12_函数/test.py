# # a = 100
#
#
# def func(b):
#     a = 10
#
#     def inner_func():
#         # a = 1
#         print(max, b)
#
#     # inner_func()
#
#     return inner_func
#
#
# # 调用外部函数
# f = func(7)
#
# f()
#
#
# def zhuang(func):
#     def wrapper(*args, **kwargs):
#         func()  # 原函数
#         print('----------')
#
#     return wrapper
#
#
# @zhuang
# def f1():
#     pass

from functools import reduce
tuple2 = (1,2,3)

result = reduce(lambda x, y: x - y, tuple2)
print(result)