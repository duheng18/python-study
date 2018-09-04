# 序列是具有先后关系的一组元素
# 序列类型是一个基本类型，衍生出字符串类型、元组类型、列表类型
# x in s x是否在序列s当中  x not in s
# s+t 连接两个序列和t
# s*n n*s将序列复制n次
# s[i]索引，返回s中的第i个元素，i是序列的序号
# s[i:j:k]返回序列s中第i到j以k为步长的元素子序列

# len(s)返回序列S的长度
# min（s）返回序列S的最小元素，s中元素需要可比较
# max（s）返回序列S的最大元素，s中元素需要可比较
# s.index(x) or s.index(x,i,j) 返回s从i开始到j位置中第一次出现元素x的位置
# s.count(x)返回序列s中出现x的总次数

# 序列类型应用场景
# 元组用于元素不改变的应用场景，更多用于固定搭配场景
# 列表更加灵活，它是最常见的序列类型

# 序列类型应用场景
# 元素遍历：列表 元组
# for item in ls：
#   <语句块>
# for item in tp：
#   <语句块>



ls = ["python", 123, ".io"]
print(ls[::-1])
s = "python123.io"
print(s[::-1])
print(len(s))
print(s.index("i"))
print(max(s))

# 序列类型应用场景
# 数据保护 如果不希望数据被程序所改变，转换程元组类型
ls = ["cat", "dog", "tiger", 1024]
lt = tuple(ls)
print(lt)
