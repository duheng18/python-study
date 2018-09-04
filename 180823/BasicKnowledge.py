# 原始字符串
print('Hello,\nworld!')
path = 'C:\nowhere'
print(path)
path = 'C:\\Program Files\\fnord\\foo\\bar\\baz\\frpzz\bozz'
print(r'C:\nowhere')
print(r'C:\\Program Files\\fnord\\foo\\bar\\baz\\frpzz\bozz')
print(r'Let\'s go!')
print(r"This is illegal")
print(r'C:\\Program Files\foo\bar''\\')
# 长字符
print('''This is a very long string.It continues here.And it's not over yet."Hello,world"Still here.''')
print("Hello,\
      word!")
print( \
    "Hello,world")
# 字符串拼接
print(repr("Hello,world!"))
print(str("Hello,world!"))
print(repr(1000000000000000))
temp = 42
print("The temperature is " + repr(temp))
print("The temperature is " + str(temp))
print("The temperature is {}".format(temp))
