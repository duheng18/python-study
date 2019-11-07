import re

path = input('请输入文件路径:')  # 获取要读取的文件路径如 E:/1.txt
with open(path, 'r') as f:  # 从文件中读取数据，并赋值给text(我的这个写法是简便的写法，不用写f.close（）)
    text = f.read()
rg = re.compile('ADJECTIVE|NOUN|ADVERB|VERB')  # 创建正则表达式
while 1:  # 循环替换文本中的词,即text中的数据
    if rg.search(text):  # 判断text中是否有匹配的词，如果有返回为真
        x = rg.search(text).group().lower()  # 调用group()方法返回匹配的字符串如：'ADJECTIVE',并将它转换为小写，然后赋值给变量x
        print('Enter an %s:' % x)  # 提示用户输入替换的词
        word = input()  # 输入单词,赋值给变量word
        text = rg.sub(word, text, count=1)  # 替换text中的匹配的词，只替换一个，不是所有
    else:  # text中没有匹配的词，退出循环
        break

path = input('请输入文件路径:')  # 输入你希望产生新文件的路径
with open(path, 'a') as f:  # 将修改后的字符串写入到新文件
    f.write(text)
