from tkinter import *
import time
from sys import exit


class RandomName(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.name_lists = []
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()


    def read_txt(self, path):
        self.name_lists = []
        with open(path, 'r', encoding='utf-8') as f:
            names = f.readlines()
            for name in names:
                self.name_lists.append(name)
        return self.name_lists

    def makeWidgets(self):
        #  定义标签栏
        l = Label(self, textvariable=self.timestr, font=("Arial, 100"))
        self.name_lists = self.read_txt('student.txt')
        self.set_name(self._elapsedtime)
        l.pack(side=TOP)

    def update(self):
        # 更新显示内容
        self._elapsedtime = time.time() - self._start
        self.set_name(self._elapsedtime)  # 设置显示内容
        self._timer = self.after(50, self.update)  # 刷新界面

    def set_name(self, elap):
        # 随机产生姓名
        cur = int(elap * 100 % 30)
        self.timestr.set(self.name_lists[cur])

    def Start(self):
        # 开始
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self.update()
            self._running = True

    def Stop(self):
        # 暂停
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self.set_name(self._elapsedtime)
            self._running = False

    def Exit(self):
        # 暂停
        if not self._running:
            exit()

    def name_label(self):
        # 显示窗口
        self.pack(side=TOP)
        Button(self, text='start', command=self.Start, width=20, height=4).pack(side=LEFT)
        Button(self, text='stop', command=self.Stop, width=20, height=4).pack(side=LEFT)
        Button(self, text='exit', command=self.Exit, width=20, height=4).pack(side=LEFT)



