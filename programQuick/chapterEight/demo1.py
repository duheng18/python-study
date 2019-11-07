import re

path=input('请输入路径：')
with open(path,'r') as f:
    file=f.read()
regex=re.compile('ADJECTIVE|NOUN|ADVERB|VERB')
while 1:
    if regex.search(file):
        x=regex.search(file).group().lower()
        print('Enter an %s',x)
        word=input()
        file=regex.sub(word,file,count=1)
    else:
        break

path0=input("请输入路径：")
with open(path0,'a') as f:
    f.write(file)
print(file)
