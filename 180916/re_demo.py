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
print(re.split('[,]+', some_text, maxsplit=3))
# ['alpha', 'beta', 'gamma delta']
pat = '[a-zA-Z]+'
text = '"Hm...Err -- are you sure?" he said, sounding insecure.'
print(re.findall(pat,text))
# ['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
pat0=r'[.?\-",]+'
print(re.findall(pat0,text))
# ['"', '...', '--', '?"', ',', '.']