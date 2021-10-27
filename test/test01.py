# day02语言元素

"""华氏度转摄氏度

Version 0.1
Author:xhz
"""
import msvcrt
print("Welcome to use this tool!")
flag1 = False
flag2 = False
flag3 = True
while flag3:
    f = float(input("Plz input you HSD:(Only float or int will be accept!)"))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))


# 判断是否是闰年
# 年份对4取余没有余数，/100 ！=0   世纪年除以400，能被整除就是闰年。
year = int(input("请输入年份："))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
if is_leap:
    print("%d是闰年！" % year)
else:
    print("%d不是闰年！" % year)

"""
输入半径计算圆的周长和面积

Version: 0.1
Author: xhz
"""
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

