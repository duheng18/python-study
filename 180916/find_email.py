# 要列出邮件头中提及的所有邮件地址，需要创建一个只与邮件地址匹配的正则表达式，然后使用方法findall找出所有与之匹配的内容。
# 为避免重复，可将邮件地址存储在本章前面介绍的集合中。最后，提取键，将它们排序并打印出来。
import fileinput, re

pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
addresses = set()
for line in fileinput.input():
    for address in pat.findall(line):
        addresses.add(address)
for address in sorted(addresses):
    print(address)

#   $ python find_email.py message.eml
#   Mr.Gumby@bar.baz foo@bar.baz foo@baz.com magnus@bozz.floop
