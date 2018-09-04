# 调用jieba库
import jieba

# 打开文件
txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
# 对文件进行分词处理，形式一个列表类型的带有所有单词的列表
words = jieba.lcut(txt)
# 构造一个字典counts
counts = {}
# 逐一遍历words中的每一个中文单词，并将中文单词进行处理
for word in words:
    if len(word) == 1:
        continue
    else:
        # 通过字典来进行计数
        counts[word] = counts.get(word, 0) + 1
# 将带有计算的字典counts转换成列表
items = list(counts.items())
# 对列表进行排序
items.sort(key=lambda x: x[1], reverse=True)
# 将前15位单词打印输出
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
