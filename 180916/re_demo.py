import re

some_text = 'alpha,beta,,,,gamma delta'
# split允许用字符串','的匹配来分割字符串，而re.split则允许用任意长度的逗号和空格序列来分割字符串。
print(re.split('[,]+', some_text))
# ['alpha', 'beta', 'gamma', 'delta']
# 如果模式包含小括号，那么括起来的字符组合会散布在分割后的子字符串之间。
print(re.split('o(o)', 'foobar'))
# ['f', 'o', 'bar']
print(re.split('[,]', some_text))
# ['alpha', 'beta', '', '', '', 'gamma delta']
# maxsplit参数表示字符串最多可以分割的次数。
print(re.split('[,]+', some_text, maxsplit=1))
# ['alpha', 'beta,,,,gamma delta']
print(re.split('[,]+', some_text, maxsplit=2))
# ['alpha', 'beta', 'gamma delta']
pat = '[a-zA-Z]+'
text = '"Hm...Err -- are you sure?" he said, sounding insecure.'
print(re.findall(pat, text))
# ['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
# 横线（-）被转义了，不会将其解释为字符范围的一部分（比如a~z）。
pat0 = r'[.?\-",]+'
print(re.findall(pat0, text))
# ['"', '...', '--', '?"', ',', '.']

# 函数re.sub的作用在于：使用给定的替换内容将匹配模式的子字符串（最左端并且非重叠的子字符串）替换掉。
pat1 = '{name}'
text1 = 'Dear {name}...'
print(re.sub(pat1, 'Mr. Gumby', text1))
# Dear Mr. Gumby...

# re.escape可以对字符串中所有可能被解释为正则运算符的字符进行转义的应用函数。
print(re.escape('www.python.org'))
# www\.python\.org
print(re.escape('But where is the ambiguity?'))
# But\ where\ is\ the\ ambiguity\?
