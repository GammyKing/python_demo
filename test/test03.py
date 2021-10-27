# day05构造程序逻辑
"""水仙花数"""
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     result = low ** 3 + mid ** 3 + high ** 3
#     if result == num:
#         print(result)
#
"""数值反转"""


# start = int(input("请输入一个数值："))
# result = 0
# while start > 0:
#     result = result * 10 + start % 10
#     start //= 10
# print(result)

# money = 100
# for a in range(0, 20):
#     for b in range(0, 33):
#         c = 100 - a - b
#         if a * 5 + b * 3 + c / 3 == 100:
#             print("big:%.1f mid:%.1f little:%.1f" % (a, b, c))
# from random import randint
#
#
# def shock_nodes():
#     a = randint(0, 6)
#     b = randint(0, 6)
#     return int(a + b)
#
#
# money = 1000
# while money > 0:
#     print("Your money is:", money)
#     need_to_go = False
#     while True:
#         debt = int(input("请下注："))
#         if 0 < debt <= money:
#             break
#     first = shock_nodes()
#     print("第一轮数值：", first)
#     if first == 7 or first == 11:
#         print("玩家胜利！")
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print("庄家胜利！")
#         money -= debt
#     else:
#         need_to_go = True
#     while need_to_go:
#         print("进入第二轮下注！")
#         second = shock_nodes()
#         print("第二轮数值：", second)
#         if second == 7:
#             print("庄家胜利！")
#             money -= debt
#             need_to_go = False
#         elif second == first:
#             print("玩家胜利！")
#             money += debt
#             need_to_go = False
#         else:
#             need_to_go = True
# print("你输光了所有的钱！")
x = int(input())
a = 1
b = 1
while n <= x: