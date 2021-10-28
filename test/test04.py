# 函数和模块的使用
"""
输入M和N计算C（M，N）

Version:0.1
Author:xhz
"""


# def fac(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result
#
#
# m = int(input('M = '))
# n = int(input('N = '))
# print(fac(m) // fac(n) // fac(m - n))

# 关于函数重载内容
# from random import randint
#
#
# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     """三数相加"""
#     return a + b + c
#
#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))

# 实现计算求最大公约数和最小公倍数的函数
# one = int(input("输入a:"))
# two = int(input("输入b:"))
#
#
# def max_num(a, b):
#     min = a if a < b else b
#     max = a if a > b else b
#     while 1:
#         if max % min == 0:
#             print('最大公约数：', min)
#             print('最小公倍数：', max)
#             break
#         for i in range(int(min / 2), 1, -1):
#             if a % i == 0 and b % i == 0:
#                 print('最大公约数为：', i)
#                 break
#         for x in range(max, min * max + 1):
#             if x % min == 0 and x % max == 0:
#                 print('最小公倍数为：', x)
#                 break
#         break
#
#
# max_num(one, two)

# # 回文数
# def huiwen(a):
#     num = a
#     result = 0
#     while num > 0:
#         result = result * 10 + num % 10
#         num //= 10
#     if result == a:
#         return result
#
#
# # 判断一个数是不是素数的函数
# def is_sushu(num):
#     if num <= 2:
#         return True
#     else:
#         for i in range(2, int(num / 2) + 1):
#             if num % i == 0:
#                 return False
#     return True


# # 判断是不是一个回文素数
# def is_huiwen_sushu(num):
#     a = num
#     total = 0
#     flag = False
#     while num > 0:
#         total = total * 10 + num % 10
#         num //= 10
#     if total == num:
#         flag = True
#     if flag:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#

#
# num = int(input('请输入正整数：'))
# if huiwen(num) and is_sushu(num):
#     print('%d是回文素数' % num)
# else:
#     print('%d不是回文素数' % num)
