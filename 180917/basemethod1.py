f = open(r'/Users/duheng/Documents/project/python/180917/somefile3.txt', 'w')
# 使用了print来写入文件，这将自动在提供的字符串后面添加换行符。
print('First', 'line', file=f)
print('Second', 'line', file=f)
print('Third', 'and final', 'line', file=f)
f.close()
# 对打开的文件进行序列解包，从而将每行存储到不同的变量中。(这种做法不常见，因为通常不知道文件包含多少行，但这演示了文件对象是可迭代的。)
# 写入文件后将其关闭，以确保数据得以写入磁盘。(如你所见，读取文件后并没有将其关闭。这可能有点粗糙，但并非致命的。)
lines = list(open('somefile3.txt'))
print(lines)
# ['First line\n', 'Second line\n', 'Third and final line\n']

first, second, third = open('somefile3.txt')
print(first)
# First line
print(second)
# Second line
print(third)
# Third and final line
