from tkinter import *
from tkinter.scrolledtext import ScrolledText


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

# 知识要点：
# 一、pack()
# 参数side：指定将控件停靠在哪一条边上,LEFT、RIGHT、TOP或BOTTOM
# 参数expand：让控件随父控件（这里是窗口）一起增大，可将expand设为True
# 二、ScrolledText控件
# 编辑区域
# 三、Entry控件
# 要提取Entry控件的内容，可以使用get方法
# 四、Button控件
# 参数text：设置控件的名字
# 参数command：控件的事件处理，注意，command传递参数是使用lambda:，否则控件自动执行
