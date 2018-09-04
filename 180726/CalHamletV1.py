# 获得一个文本的具体信息
def getText():
    # 打开一个文件
    txt = open("hamlet.txt", "r").read()
    # 为了避免大小写对词频统计的干扰，将所有的英文字母变成小写
    txt = txt.lower()
    # 获得文本中出现的各种特殊符号
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_＇{|}~':
        # 将特殊符号替换为空格
        txt = txt.replace(ch, "")
    # 文本的所有单词都是小写的，单词与单词直接使用空格来分隔，而且没有任何特殊符号
    # 获得规范化的文本
    return txt


# 对文件进行读取，并对文本进行规划
hamletTxt = getText()
# 默认采用空格将字符串中的信息进行分隔，并且以列表形式返回给变量
# words是一个列表类型，里面每一个元素都是一个以空格分开的单词
words = hamletTxt.split()
# 对每个单词进行出现次数的标记，单词：出现的次数（出现的频率）
# 空字典
counts = {}
# 逐一从words这个列表中取出每一个元素
for word in words:
    # 确认元素是否再counts中
    # 字典的.get方法用来从字典中获得某一个键对应的值，如果这个键未在字典中，我们给出默认值.
    # 用当前的某一个英文单词作为键索引字典，如果它在里面就返回次数，后面+1说明这个单词又出现了一次，
    # 如果这个单词不在字典中，那我们就把它加到字典中，并且赋给当前的值为0，0+1是1
    #
    counts[word] = counts.get(word, 0) + 1
# 对词频出现的次数进行排序，将字典类型转换程列表类型便于操作
#print(counts)
items = list(counts.items())
#print(items)
# sort方法参数lambda用来指定再列表中指定哪一个多元选项的列作为排序列，默认排序方式是从小到大。
# 对于一个列表，按照键值对的两个元素的第二个元素排序，排序方式由大到小
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    #前10个对应的单词以及次数打印出来
    print("{0:<10}{1:>5}".format(word, count))
print(items)
