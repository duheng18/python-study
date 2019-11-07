# 列表：以中括号[]开头结尾，数据通过逗号,隔开，使用引号.
# 主要方法：长度，增删改查（输入某一或几个）,反转，排序
print(dir(list))
# ['__add__', '__class__', '__contains__', '__delattr__'
# , '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__',
# '__imul__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__',
# '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse',
# 'sort']
book = ["python", "java", "Appium", "selenium"]
# 1.输出book列表中第2个book[1]
print(book)
print(book[1])
# 2.列表的长度len(book)
print(len(book))
# 3.在后面追加数据book.append
book.append("today history")
book.append("tomorrow history")
print(book)
# 4.删除第3个数据book.pop
book.pop(2)
print(book)
# 5.将数据插入第3位置book.insert(2,"d")
book.insert(2, "furture history")
print(book)
# 6.在列表后面追加另一个列表book.extend()
book.extend(book)
print(book)
# 7.在列表中找到并删除一个特定项book.remove("")
book.remove("tomorrow history")

book.pop()  # 删除最后一个
print(book)
print(book.copy() * 4 + book)  # 拷贝3遍+一遍
print(book.copy().clear())  # 删除全部
print(book)
book=['Google','testerhome','testing-studio','Baidu']
# 8.将列表顺序反转book.reverse()
book.reverse()
print("列表反转后：", book)
# 9.将列表排序book.sort()
book.sort()
print("列表排序后", book)
