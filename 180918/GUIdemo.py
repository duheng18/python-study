from tkinter import *
from tkinter.scrolledtext import ScrolledText


def load():
    with open(filename) as file:
        contents.delete('1.0', END)
    contents.insert(INSERT, file.read())


def save():
    with open(filename, 'w') as file:
        file.write(contents.get('1.0', END))


top = Tk()
top.title("Simple Editor")
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

mainloop()

# 你可按如下步骤来尝试使用这个文本编辑器
# (1) 运行这个程序
# (2) 在大型文本区域中输入一些内容，如Hello, world!。
# (3) 在小型文本框中输入一个文件名，如hello.txt。请确保指定的文件不存在，否则原有文件
# 将被覆盖掉。
# 4) 单击Save按钮。
# (5) 退出程序。
# (6) 再次启动程序。
# (7) 在小型文本框中输入刚才输入的文件名。
# (8) 单击Open按钮，这个文件包含的文本将出现在大型文本区域中。
# (9) 随心所欲地编辑这个文件，再保存它。

