# find_sender.py
import fileinput, re

# 为提高处理效率，我编译了正则表达式。
# 将用于匹配要提取文本的子模式放在圆括号内，使其变成了一个编组。
# 使用了一个非贪婪模式，使其只匹配最后一对尖括号(以防姓名也包含尖括号)。
# 使用了美元符号指出要使用这个模式来匹配整行(直到行尾)。
# 使用了if语句来确保匹配后才提取与特定编组匹配的内容。
pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
if m: print(m.group(1))
# 可像下面这样运行这个程序(假设电子邮件保存在文本文件message.eml中): $ python find_sender.py message.eml
# Foo Fie
