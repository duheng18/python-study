import re

# 重复运算符默认是贪婪的，这意味着它们将匹配尽可能多的内容。例如，假设重写了 前面的突出程序，在其中使用了如下模式:
emphasis_pattern = r'\*(.+)\*'
print(re.sub(emphasis_pattern, r'<em>\1</em>', '*This* is *it*!'))
# <em>This* is *it</em>!
# 这个模式匹配了从第一个星号到最后一个星号的全部内容，其中包含另外 5 两个星号!这就是贪婪的意思:能匹配多少就匹配多少。

emphasis_pattern = r'\*\*(.+?)\*\*'
# 这里使用的是运算符+?而不是+。这意味着与以前一样，这个模式将匹配一个或多个通配 符，但匹配尽可能少的内容，因为它是非贪婪的。
print(re.sub(emphasis_pattern, r'<em>\1</em>', '**This** is **it**!'))
# <em>This</em> is <em>it</em>!
