# 分片
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
# 为了让分片部分能够包含列表的最后一个元素，必须提供最后一个元素的下一个元素所对应的索引作为边界。
print(numbers[7:10])
print(numbers[-3:-1])
# 分片中最左边的索引比它右边的晚出现在序列中，结果就是一个空的序列
print(numbers[-3:0])
# 如果分片所得部分包括序列结尾的元素，那么只需置空最后一个索引即可。
print(numbers[-3:])
# 序列开始的元素
print(numbers[:3])
# 复制整个序列
print(numbers[:])
# print(numbers)

# 分片示例
# 对http://www.something.com形式的URL进行分隔
# url = input('Please enter the URL:')
# domain = url[11:-4]
# print("Domain name:" + domain)

# 开始点的元素包括在结果之中，而结束点的元素则不在分片之内
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[::4])
# 步长为负数，分片从右到左提取元素
# 当使用一个负数作为步长时，必须让开始点（开始索引）大于结束点。
# 对于一个正数步长，Python会从序列的头部开始向右提取元素，至到最后一个元素；
# 而对于负数步长，则是从序列的尾部开始向左提取元素直到第一个元素。
print(numbers[8:3:-1])
print(numbers[10:0:-2])
print(numbers[0:10:-2])
print(numbers[::2])
print(numbers[5::-2])
print(numbers[:5:-2])
