import re

anyend='.end'
m=re.match(anyend,'bend')
if m is not None:print('bend-'+m.group())

m=re.match(anyend,'end')  #未匹配成功，end前面缺一个字符
if m is not None:print('end-'+m.group())

m=re.match(anyend,'\nend') #未匹配成功end前面有换行符
if m is not None:print('\n-'+m.group())

m=re.search('.end','the end.') #在搜索中匹配'' 匹配空字符串
if m is not None:print('end-'+m.group())