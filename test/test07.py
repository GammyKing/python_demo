# 面向对象高阶训练题
# 凹凸曼打小怪兽
# from abc import ABCMeta, abstractmethod
# from random import randint, randrange
#
#
# class Fighter(object, metaclass=ABCMeta):
#     """战斗者"""
#     # 通过__SLOTS__魔法限定对象可以绑定的成员变量。
#     __slots__ = ('_name', '_hp')
#
#     def __init__(self, name, hp):
#         """
#         初始化方法
#         :param name: 名字
#         :param hp: 生命值
#         """
#         self._name = name
#         self._hp = hp
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def hp(self):
#         return self._hp
#
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0
#
#     @property
#     def alive(self):
#         return self._hp > 0
#
#     @abstractmethod
#     def attack(self, other):
#         """攻击"""
#         pass
#
#
# class Ultraman(Fighter):
#     """奥特曼"""
#     __slots__ = ('_name', '_hp', '_mp')
#
#     def __init__(self, name, hp, mp):
#         """初始化方法"""
#         super().__init__(name, hp)
#         self._mp = mp
#
#     def attack(self, other):
#         other.hp -= randint(15, 25)
#
#     def huge_attack(self, other):
#         """
#         究极必杀技(带到对方至少50点或者四分三血量
#         :param other: 被击杀对象
#         :return: 使用成功就true否则false
#         """
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp * 3 // 4
#             injury = injury if injury >= 50 else 50
#             return True
#         else:
#             self.attack(other)  # 普攻
#             False
#
#     def resume(self):
#         """恢复魔法值"""
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point
#
#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name + \
#                '生命值: %d\n' % self._hp + \
#                '魔法值: %d\n' % self._mp
#
#
# class Monster(Fighter):
#     """
#     小怪兽
#     """
#     __slots__ = ('_name', '_hp')
#
#     def attack(self, other):
#         other._hp -= randint(10, 20)
#
#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name + \
#                '生命值: %d\n' % self._hp
#
#
# def is_any_alive(monsters):
#     """
#     判断有没有小怪物还活着
#     :param monsters: 怪物
#     :return: 怪物
#     """
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False
#
#
# def select_alive_one(monsters):
#     """选中一只活着的小怪兽"""
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster
#
#
# def display_info(ultraman, monsters):
#     """显示奥特曼和小怪兽"""
#     print(ultraman)
#     for monster in monsters:
#         print(monster, end='')
#
#
# def main():
#     u = Ultraman('骆昊', 1000, 120)
#     m1 = Monster('狄仁杰', 250)
#     m2 = Monster('白元芳', 500)
#     m3 = Monster('王大锤', 750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_alive(ms):
#         print('========第%02d回合========' % fight_round)
#         m = select_alive_one(ms)  # 选中一只小怪兽
#         skill = randint(1, 10)  # 通过随机数选择使用哪种技能
#         if skill <= 6:  # 60%的概率使用普通攻击
#             print('%s使用普通攻击打了%s.' % (u.name, m.name))
#             u.attack(m)
#             print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
#             if u.magic_attack(ms):
#                 print('%s使用了魔法攻击.' % u.name)
#             else:
#                 print('%s使用魔法失败.' % u.name)
#         else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
#             if u.huge_attack(m):
#                 print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
#             else:
#                 print('%s使用普通攻击打了%s.' % (u.name, m.name))
#                 print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
#             print('%s回击了%s.' % (m.name, u.name))
#             m.attack(u)
#         display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
#         fight_round += 1
#     print('\n========战斗结束!========\n')
#     if u.alive > 0:
#         print('%s奥特曼胜利!' % u.name)
#     else:
#         print('小怪兽胜利!')
#
#
# if __name__ == '__main__':
#     main()


# 扑克游戏
# import random
#
#
# class Card(object):
#     """一张牌"""
#
#     def __init__(self, suite, face):
#         self._suite = suite
#         self._face = face
#
#     @property
#     def face(self):
#         return self._face
#
#     @property
#     def suite(self):
#         return self._suite
#
#     def __str__(self):
#         if self._face == 1:
#             face_str = 'A'
#         elif self._face == 11:
#             face_str = 'J'
#         elif self._face == 12:
#             face_str = 'Q'
#         elif self._face == 13:
#             face_str = 'K'
#         else:
#             face_str = str(self._face)
#         return '%s%s' % (self._suite, face_str)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Poker(object):
#     """一副牌"""
#
#     def __init__(self):
#         self._cards = [Card(suite, face)
#                        for suite in '♠♥♣♦'
#                        for face in range(1, 14)]
#         self._current = 0
#
#     @property
#     def cards(self):
#         return self._cards
#
#     def shuffle(self):
#         """洗牌（随机乱序）"""
#         self._current = 0
#         random.shuffle(self._cards)
#
#     @property
#     def next(self):
#         """发牌"""
#         card = self._cards[self._current]
#         self._current += 1
#         return card
#
#     @property
#     def has_next(self):
#         """还没有牌"""
#         return self._current < len(self._cards)
#
#
# class Player(object):
#     """玩家"""
#
#     def __init__(self, name):
#         self._name = name
#         self._cards_on_hand = []
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def cards_on_hand(self):
#         return self._cards_on_hand
#
#     def get(self, card):
#         """摸牌"""
#         self._cards_on_hand.append(card)
#
#     def arrange(self, card_key):
#         """玩家整理手上的牌"""
#         self._cards_on_hand.sort(key=card_key)
#
#     # 排序规则-先根据花色再根据点数排序
#
#
# def get_key(card):
#     return (card.suite, card.face)
#
#
# def main():
#     p = Poker()
#     p.shuffle()
#     players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
#     for _ in range(13):
#         for player in players:
#             player.get(p.next)
#     for player in players:
#         print(player.name + ':', end=' ')
#         player.arrange(get_key)
#         print(player.cards_on_hand)
#
#
# if __name__ == '__main__':
#     main()

# 工资结算系统
# from abc import ABCMeta, abstractmethod
#
#
# class Employee(object, metaclass=ABCMeta):
#     """员工"""
#
#     def __init__(self, name):
#         """
#         初始化方法
#         :param name: 姓名
#         """
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @abstractmethod
#     def get_salary(self):
#         """
#         获得薪水
#         :return: 月薪
#         """
#         pass
#
#
# class Manager(Employee):
#     """
#     部门经理
#     """
#
#     def get_salary(self):
#         return 15000.0
#
#
# class Programmer(Employee):
#     """程序员"""
#
#     def __init__(self, name, working_hour=0):
#         super().__init__(name)
#         self._working_hour = working_hour
#
#     @property
#     def working_hour(self):
#         return self._working_hour
#
#     @working_hour.setter
#     def working_hour(self, working_hour):
#         self._working_hour = working_hour if working_hour > 0 else 0
#
#     def get_salary(self):
#         return 150.0 * self._working_hour
#
#
# class Saleman(Employee):
#     """销售员"""
#
#     # 定义销售量
#     def __init__(self, name, sale_mount=0):
#         super().__init__(name)
#         self._sale_mount = sale_mount
#
#     @property
#     def sale_mount(self):
#         return self._sale_mount
#
#     @sale_mount.setter
#     def sale_mount(self, sale_mount):
#         self._sale_mount = sale_mount if sale_mount > 0 else 0
#
#     def get_salary(self):
#         return 1200 + 0.05 * self._sale_mount
#
#
# def main():
#     # python中的集中数据结构的清算：
#     # () 表示：元组数据
#     # [] 表示：list列表数据类型
#     # {} 表示：字典类型
#     emps = [
#         Manager('john'), Programmer('jack'),
#         Manager('tom'), Saleman('mas'),
#         Saleman('jjj'), Programmer('ttt'),
#         Programmer('dd')
#     ]
#     # 用列表的形式将数据装进去，用is_instance来判断对象类型
#     for emp in emps:
#         if isinstance(emp, Programmer):
#             emp.working_hour = int(input('请输入%s本月工作时长：' % emp.name))
#         elif isinstance(emp, Saleman):
#             emp.sale_mount = float(input('请输入%s本月销售量：' % emp.name))
#         print('%s本月工资为：￥%s元' %
#               (emp.name, emp.get_salary()))
#
#
# if __name__ == '__main__':
#     main()
