import re

s = "adfad asdfasdf asdfas asdfawef asd adsfas "

reObj1 = re.compile('((\w+)\s+\w+)')
print(reObj1.findall(s))
# [('adfad asdfasdf', 'adfad'), ('asdfas asdfawef', 'asdfas'), ('asd adsfas', 'asd')]

reObj2 = re.compile('(\w+)\s+\w+')
print(reObj2.findall(s))
# ['adfad', 'asdfas', 'asd']

reObj3 = re.compile('\w+\s+\w+')
print(reObj3.findall(s))
# ['adfad asdfasdf', 'asdfas asdfawef', 'asd adsfas']

pat = '[a-zAZ]+'
string = 'abdces'
if re.search(pat, string):
    print('Fount it!')
