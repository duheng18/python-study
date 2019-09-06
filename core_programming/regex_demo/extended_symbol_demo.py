import re

# ['yes', 'Yes', 'YES'] 忽略大小写
print(re.findall(r'(?i)yes', 'yes？Yes. YES!!'))

# ['The', 'through', 'this'] 忽略大小写
print(re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.'))

# ['This line is the first', 'that line'] 忽略大小写 使用‘m’实现跨行搜索，一行为单个实体
print(re.findall(r'(?im)(^th[\w ]+)', """This line is the first,\nanother line,\nthat line, it's the best\n"""))

# ['the second line', 'the third line']
print(re.findall(r'th.+', """The first line,\nthe second line\nthe third line\n"""))

# ['the second line\nthe third line\n']
print(re.findall(r'(?s)th.+', """The first line,\nthe second line\nthe third line\n"""))

# print(re.search(r'''(?x)\((\d{3})\)\[\]\(\d{3}\)\-\(\d{4}\)''', '(800) 555-1212').groups())


# ['google.com', 'google.com', 'google.com']
print(re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://google.com http://www.google.com http://code.google.com'))

print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})=(?:\d{4})','(800) 555-1212').groupdict())