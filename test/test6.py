# 面向对象编程基础
# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print('%slearning%s.' % (self.name, course_name))
#
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能看熊出没.' % self.name)
#         else:
#             print('%s正在看岛国爱情动作大电影.' % self.name)
#
#
# def main():
#     stu1 = Student('xhz', 38)
#     stu1.study('Python程序设计')
#     stu1.watch_movie()
#     stu2 = Student('wxz', 15)
#     stu2.study('思想品德')
#     stu2.watch_movie()
#
#
# if __name__ == '__main__':
#     main()

# 访问可见性问题
# class Test:
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):  # 利用双下划线作为开头，能够使得该方法私有化。
#         print(self.__foo)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#     test.__bar()
#     print(test.__foo)
#
#
# if __name__ == '__main__':
#     main()

# 验证私有方法
# class Test:
#
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#     test._Test__bar()
#     print(test._Test__foo)
#
#
# if __name__ == "__main__":
#     main()
# def main():
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']
#     subjs = ['语文', '数学', '英语']
#     scores = [[]] * 5
#     for row, name in enumerate(names):
#         print('请输入%s的成绩' % name)
#         scores[row] = [0] * 3
#         for col, subj in enumerate(subjs):
#             scores[row][col] = float(input(subj + ': '))
#     print(scores)
#
#
# if __name__ == '__main__':
#     main()
# 面向对象练习题：时钟
# from time import sleep
#
#
# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """
#         初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         """
#         走字
#         :return:
#         """
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)
#
#
# def main():
#     clock = Clock(23, 59, 59)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     main()

# 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
# from math import sqrt
#
#
# # 描述平面上两点之间的距离的类
#
# class Point(object):
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         """
#         移动到的点
#         :param x:
#         :param y:
#         :return:
#         """
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         """
#         移动的横竖增量
#         :param dx:
#         :param dy:
#         :return:
#         """
#         self.x += dx
#         self.y += dy
#
#     def distinct_to(self, other):
#         """
#         与另外一个点的横竖差距
#         :param other:
#         :return:
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s,%s)' % (str(self.x), str(self.y))
#
#
# def main():
#     p1 = Point(1, 2)
#     p2 = Point(0, 0)
#     p2.move_by(2, 3)
#     print(p1.distinct_to(p2))
#
#
# if __name__ == '__main__':
#     main()
# class Person(object):
#     # 限定Person对象只能绑定_name,_age,_gender
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     # 访问器 -getter方法
#     @property
#     def name(self):
#         return self._name
#
#     # 访问器 --setter方法
#     @property
#     def age(self):
#         return self._age
#
#     # 修改器 --setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#     def play(self):
#         if self._age <= 16:
#             print("%s正在玩儿飞行棋。" % self._name)
#         else:
#             print("%s正在玩儿斗地主。" % self._name)
#
#
# def main():
#     person = Person('www', 12)
#     person.play()
#     person.name = 'qqq'
#     person.age = 22
#     person.play()
#
#
# if __name__ == '__main__':
#     main()
# 构建三角形
# from math import sqrt
#
#
# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def isvalid(a, b, c):
#         return a + b > c and a + c > b and b + c > a
#
#     # 计算周长
#     def circle(self):
#         return self._a + self._b + self._c
#
#     # 计算面积
#     def area(self):
#         half = 1 / 2 * self.circle()
#         return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))
#
#
# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法和类方法都是通过给类发送消息来调用的
#     if Triangle.isvalid(a, b, c):
#         t = Triangle(a, b, c)
#         # 也可以通过类发消息来调用对象方法但是要传入接受消息的对象作为参数
#         # print（Triangle.circle(t))
#         print(Triangle.circle(t))
#         print(t.circle())
#         print(t.area())
#     else:
#         print("Can not make it as Triangle!")
#
#
# if __name__ == '__main__':
#     main()

# from time import time, localtime, sleep
#
#
# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
#
# def main():
#     # 通过类方法创建对象并获取系统时间
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     main()

# 类之间的关系
# 简单来说，类之间的关系有三种：is-a/has-a/use-a
# is-a关系也叫继承或泛化。例如学生和人
# has-a通常称之为关联。比如部门和员工之间的关系，汽车和引擎之间的关系都属于关联关系；
# 关联关系如果是整体和部分的，我们称之为 聚合关系
# 如果整体进一步负责了部分的生命周期（整体部分是不可分割的，同时存在也同时消亡。）那么这种就是最强的关联关系
# 我们称之为合成关系。
# use-a通常称为依赖关系，比如司机有一个驾驶的行为（方法），其中（的参数） 使用到了汽车，那么司机和汽车的关系就是依赖关系。

# 继承与多态
class Person(object):
    """human"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age > 16:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


# 学生 继承 人
class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    # 新建了方法，并且多加了功能
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_av()


# if __name__ == '__main__':
#     main()
# 子类重写父类方法
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """make sound"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s:汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
