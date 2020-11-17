from unittest import TestCase
from random_name import RandomName, Tk
import tkinter


class TestRandomName(TestCase):

    def test_read_txt(self):
        path = 'student.txt'
        res = RandomName().read_txt(path)
        print(res)



    def test_make_widgets(self):
        root = Tk()
        root.title("15班点名")
        root.geometry('1000x750')
        RandomName(root).makeWidgets()
        root.mainloop()

    def test_update(self):
        self.fail()

    def test_set_name(self):
        self.fail()

    def test_start(self):
        self.fail()

    def test_stop(self):
        self.fail()

    def test_exit(self):
        self.fail()

    def test_name_label(self):
        root = Tk()
        sw = RandomName()
        sw.name_label()
        root.mainloop()

