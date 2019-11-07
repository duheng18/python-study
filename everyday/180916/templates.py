# templates.py
import fileinput, re

# 与使用方括号括起的字段匹配
# 定义一个用于匹配字段的模式。
field_pat = re.compile(r'\[(.+?)\]')
# 我们将把变量收集到这里:
# 创建一个用作模板作用域的字典。
scope = {}


# 用于调用re.sub:
def replacement(match):
    # （1）从match中获取与编组1匹配的内容，并将其存储到变量code中。
    code = match.group(1)

    # （2）将作用域字典作为命名空间，并尝试计算code，再将结果转换为字符串并返回它。如果成功，
    #    就说明这个字段是表达式，因此万事大吉;否则(即引发了SyntaxError异常)，就进入下一步。
    try:
        # 如果字段为表达式，就返回其结果:
        return str(eval(code, scope))
    except SyntaxError:
        # 否则在当前作用域内执行该赋值语句 # 并返回一个空字符串
        # （3）在对表达式进行求值时使用的命名空间(作用域字典)中执行这个字段，并返回一个空字符串(因为赋值语句没有结果)。
        return ''


lines = []
# 获取所有文本并合并成一个字符串:
# 使用fileinput读取所有的行，将它们放在一个列表中，再将其合并成一个大型字符串。
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)
# 替换所有与字段模式匹配的内容:
#  调用re.sub来使用替换函数来替换所有与模式field_pat匹配的字段，并将结果打印出来
print(field_pat.sub(replacement, text))
