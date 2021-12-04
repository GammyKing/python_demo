# 图形用户界面和游戏开发
import tkinter
import tkinter.messagebox

# def main():
#     flag = True
#
#     # 修改标签上的字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'Hello World') \
#             if flag else ('blue', 'Goodbye, World')
#         label.config(text=msg, fg=color)
#
#     # 确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示', '确定要推出嘛？'):
#             top.quit()
#
#     # 创建顶层窗口：
#     top = tkinter.Tk()
#     # 设置窗口大小
#     top.geometry('240x160')
#     # 设置窗口标签
#     top.title('小游戏')
#     label = tkinter.Label(top, text='HelloWorld!', font='Arial -32', fg='red')
#     label.pack(expand=1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中，通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     # 开启主事件循环
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()

# 制作游戏窗口
# import pygame as pygame
#
#
# def main():
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸。
#     screen = pygame.display.set_mode((800, 800))
#     # 设置当前窗口的标签
#     pygame.display.set_caption('大球吃小球')
#     running = True
#     # 开启一个事件循环我处理发生的事情
#     while running:
#         # 从消息队列获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#
# if __name__ == '__main__':
#     main()


import pygame


# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption('大球吃小球')
#     screen.fill((242, 242, 242))
#     pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
#     pygame.display.flip()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#
# if __name__ == '__main__':
#     main()
#
# import pygame
#
#
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption('大球吃小球')
#     screen.fill((255, 255, 255))
#     ball_image = pygame.image.load('')
#     screen.blit(ball_image, (50, 50))
#     pygame.display.flip()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#
# if __name__ == '__main__':
#     main()
#

