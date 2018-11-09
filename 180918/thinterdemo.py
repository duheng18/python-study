from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import *


class Btn_def():
    """按键的功能"""

    def save(self, filename, contents):
        """保存文件"""
        try:
            with open(filename, 'w') as file:
                file.write(contents.get('1.0', END))
        except FileNotFoundError:
            pass

    def load(self, filename, contents):
        """打开文件"""
        try:
            with open(filename) as file:
                contents.delete('1.0', END)
                contents.insert(INSERT, file.read())
        except FileNotFoundError:
            pass


top = Tk()
top.title("TEXT EDITOR")

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Btn = Btn_def()
btn1 = Button(top, text='open', command=lambda: Btn.load(filename.get(), contents)).pack(side=RIGHT)
btn2 = Button(top, text='save', command=lambda: Btn.save(filename.get(), contents)).pack(side=RIGHT)

top.mainloop()
