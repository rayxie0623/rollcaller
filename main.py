from tkinter import Tk

from random_name import RandomName

if __name__ == '__main__':
    root = Tk()
    root.title("15班 V1.0")
    root.geometry('500x300')
    sw = RandomName(root)
    sw.name_label()
    root.mainloop()