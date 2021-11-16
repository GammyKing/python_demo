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
from math import sqrt


# 描述平面上两点之间的距离的类

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到的点
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动的横竖增量
        :param dx:
        :param dy:
        :return:
        """
        self.x += dx
        self.y += dy

    def distinct_to(self, other):
        """
        与另外一个点的横竖差距
        :param other:
        :return:
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(1, 2)
    p2 = Point(0, 0)
    p2.move_by(2, 3)
    print(p1.distinct_to(p2))


if __name__ == '__main__':
    main()
