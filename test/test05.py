# 字符串和常用数据结构
# str1 = 'hello world!'
# print(len(str1))
# print(str1.capitalize())
# print(str1.title())
# print(str1.upper())
# print(str1.find('or'))
# print(str1.find('shit'))
# print(str1.startswith('He'))
# print(str1.startswith('hel'))
# print(str1.center(50, '*'))
# print(str1.rjust(50, ' '))
# str2 = 'abc123456789'
# print(str2.isdigit())
# print(str2.isalpha())
# print(str2.isalnum())
# str3 = '  jackfrued@126.com '
# print(str3)
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())
# a, b = 5, 10
# print(f'{a} * {b} = {a*b}')

# # 使用列表
# list1 = [1, 3, 5, 7, 100]
# print(list1)
# list2 = ['hello'] * 3
# print(list2)
# # 通过index索引
# for index in range(len(list1)):
#     print(list1[index])
# # 通过for循环遍历循环列表元素
# for elem in list1:
#     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值。
# for index, elem in enumerate(list1):
#     print(index, elem)

# # 添加值
# list1 = [1, 3, 5, 7, 9, 100]
# # 添加元素
# list1.append(200)
# list1.insert(1, 100)
# # 合并两个列表
# # list1.extend([1000,2000])
# list1 += [1000, 2000]
# print(list1)
# # 先通过成员运算判断是否存在于列表中，如果存在就删除该元素
# if 3 in list1:
#     list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1)
# # 从指定位置删除元素
# list1.pop(0)
# list1.pop(len(list1) - 1)
# print(list1)
# list1.clear()
# print(list1)


# 与字符串相同，列表也可以做切片操作
# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# fruits1 = fruits[1:4]
# print(fruits1)
# fruits2 = fruits[:]
# print(fruits2)
# fruits3 = fruits[6]
# print(fruits3)
# fruits4 = fruits[::-1]
# print(fruits4)

# 列表的排序
# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# print(list2)
# # sorted函数返回列表排序后的拷贝不会修改传入的列表
# list3 = sorted(list1, reverse=True)
# print(list3)
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# # 给列表对象发出排序消息直接在列表对象上进行排序
# list1.sort(reverse=True)
# print(list1)

# 生成式和生成器
# f = [x for x in range(1, 10)]  # 生成式
# print(f)
# f = [x + y for x in 'ABCDEFG' for y in '1234567']
# print(f)
# f = [x ** 2 for x in range(1, 1000)]
# print(f)
# f = [x + y for x in range(1, 10) for y in range(1, 10)]
# print(f)
# # 通过生成器可以获取到数据但它不占用额外的空间
# f = (x ** 2 for x in range(1, 1000))
# print(f)
# for val in f:
#     print(val)
#
#
# # 通过yield关键字将一个普通函数改造成生成器函数
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
#
# def main():
#     for val in fib(20):
#         print(val)
#
#
# if __name__ == '__main__':
#     main()


# 使用元组
# 元组和李彪类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据
# 不同之处在于，元组的数据不能改变。
# 定义元组
# f = ('xhz', 38, True, 'fjpt')
# print(f)
# if f[3]:
#     print(f)
# for member in f:
#     print(member)
# # 如果重新给元组进行赋值，那么旧的元组就会被垃圾回收机制收回，直接创建一个新的元组。
# f = ('hyx', 20, True, 'fjzz')
# print(f)
# # 将元组转为列表
# person = list(f)
# print(person)
#
# # 转为列表之后，就可以修改了。
# person[0] = 'lxl'
# print(person)
# # 将列表转为元组
# person = ['apple', 'orange', 'watermalon', 'strawberry']
# person_tuple = tuple(person)
# print(person_tuple)
# # 为何需要存在元组和列表。因为我们在项目中尤其是多线程环境中可能会更喜欢使用的是那些不变对象，（一方面是因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单来说就是一个不变的对象要比可变的对象更加容易维护；）
# # 一个不变对象自动就是线程安全的，可以省掉处理同步化的开销。
# # 元组在创建时间和占用空间上都优于列表。


# python集合
# 与数学内容一致，交并差等等运算。就是不能有重复数据
# set1 = {1, 2, 3, 4, 5, 6}
# # print(set1)
# # print('Length =', len(set1))
# # 创建集合的构造器语法
# set2 = set(range(1, 10))
# # print(set2)
# set3 = set((1, 2, 3, 3, 2, 1))
# # print(set2, set3)
# # 创建集合的推导式语法（推导式也可以用于推导式）
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# # print(set4)
#
# # 向集合添加元素和从集合删除元素
# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set1, set2)
# print(set3.pop())
# print(set3)

# 成员的交集、并集、差集、对称差运算
# print(set1 & set2)
# print(set1 | set2)
# print(set1 - set2)
# print(set1 ^ set2)
# print(set1 <= set2)
# print(set1 >= set2)
# print(set3 <= set1)
# print(set3 >= set1)


# # 使用字典
# score = {'xhz':95,'hyx':78,'ddd':82}
# print(score)
# # 创建字典的构造器语法：
# items1=dict(one=1,two=2,three=3,four=4)
# print(items1)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a','b','c','d'],'123'))
# print(items2)
# # 创建字典的推导式语法
# items3 = {num:num **2 for num in range(1,10)}
# print(items1,items2,items3)
# print(score['xhz'])
# for key in score:
#     print(f'{key}:{score[key]}')
# # 更新字典中的元素
# score['xhz'] = 25
# score['hyx'] = 21
# print(score)
# score.update(xxx=56,pp=87) # 新增两个键值对
# print(score)
# if 'xxx' in score:
#     print(score['xhz'])
# # get方法也是通过键获取对应的值到那时可以设置默认值
# print(score.get('xhz',25))
# # 删除字典中的元素
# print(score.popitem())
# print(score.popitem())
# print(score.pop('xhz',25))
# # 清空字典
# score.clear()
# print(score)


# 作业：
# 跑马灯
# import os
# import time
#
#
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.5)
#         content = content[1:] + content[0]
#
#
# if __name__ == '__main__':
#     main()

# 验证码设计
# import random
#
#
# def generate_code(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code
#
#
# print(generate_code())

# def get_suffix(filename):
#     if '.' in filename:
#         index = filename.find('.')
#         suffix = filename[index + 1:]
#         return suffix
#     return 'plz input right string'
#
#
# f = input('请输入文件名：')
# print(get_suffix(f))

# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     return ''
#
#
# print(get_suffix('httlo.nihso', True))

# 返回数列里最大和第二大的数值。
# def find_max_min(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2
#
#
# print(find_max_min([1, 2, 3, 67, 90]))

# import time
#
# scale = 10
# print("----------start-------------")
# for i in range(scale + 1):
#     a, b = '**' * i, '...' * (scale - i)
#     c = (i / scale) * 100
#     print("%{:^3.0f}[{}->{}]".format(c, a, b))
#     time.sleep(0.1)
# print("-------------end----------------")


# 跑马灯
# import time
# import os
# content = '北京欢迎你………'
# print(content)
# while True:
#     os.system('cls')
#     time.sleep(0.2)
#     content = content[1:] + content[0]
#     print(content)


# 奥特曼打小怪兽
from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击
        """
        pass


class Ultraman(Fighter):
    """奥特曼"""
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """
        初始化方法
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True

    def magic_attack(self, others):
        """魔法攻击"""
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值: %d\n' % self._hp + \
               '魔法值: %d\n' % self._mp


class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)  # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()
