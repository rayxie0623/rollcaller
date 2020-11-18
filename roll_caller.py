import random
from tkinter import *
import tkinter as tk
import threading

class roll_caller(Frame):

    def __init__(self):
        '''
        初始化
        '''
        self.is_running = False
        self.ready = 0
        self.name_lists = []
        self.window = tk.Tk()   # 实例化建立窗口windows
        self.config()


    def config(self):
        '''
        窗口配置函数
        '''

        #窗口配置
        self.window.geometry('700x500')
        self.window.title("小仙女开始点名了... v2.0")  #名字

        #label配置
        self.var = tk.StringVar(self.window, "开始点名啦") # 用var来接收点击后传上来的信息
        label = tk.Label(self.window, textvariable=self.var, font=('Arial', 70),
                 width=30, height=2) # 设置标签
        label.pack()  # 放置标签；自动调节位置
        #设置Button
        self.button_pack()
        self.window.mainloop()

    def button_pack(self):
        '''
        放置button
        '''
        button_start = tk.Button(self.window, text='开始', font=('Arial', 30),
                                 width=10, height=2, command=self.start)
        button_start.pack(side = 'left')

        button_start = tk.Button(self.window, text='停止', font=('Arial', 30),
                                 width=10, height=2, command=self.stop)
        button_start.pack(side = 'left')

        button_start = tk.Button(self.window, text='退出', font=('Arial', 30),
                                 width=10, height=2, command=self.exit)
        button_start.pack(side = 'left')

    def start(self):
        if not self.is_running:
            self.name_lists = self.read_txt('student.txt')
            self.is_running = True
            self.thread = threading.Thread(target=self.update, args=())
            self.thread.setDaemon(True)
            self.thread.start()

    def update(self):
        while self.is_running:
            index_num = random.randint(1,10000)%len(self.name_lists)
            people = self.name_lists[index_num]
            self.var.set(people)

    def stop(self):
        if self.is_running:
            self.is_running = False

    def exit(self):
        if not self.is_running:
            sys.exit()

    def read_txt(self, path):
        self.name_lists = []
        with open(path, 'r', encoding='utf-8') as f:
            names = f.readlines()
            for name in names:
                self.name_lists.append(name)
        return self.name_lists





