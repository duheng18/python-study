# 1.实现一个函数，要求对一个列表里面所有数字求和，如果里面含有非数字的元素，直接跳过。
# 比如：[1,2,3]输出是5，如果是[1,2,4,"a"]输出是7。并在另外一个包（目录）里面调用这个函数。
def sumData(data):
    sum = 0
    for item in data:
        if isinstance(item, int) | isinstance(item, float):
            sum += item;
        else:
            continue
    print(sum)


# 2.已有字典dic={"name":"xiaozhang","sex":"male"},访问字典dic["grade"]
dic = {"name": "xiaozhang", "sex": "male"}
print(dic.get('grade'))


# try:
#     print(dic['grade'])
# except KeyError:
#     print('no key')
# 3.实现一个不定长参数的函数def flexible(aa,*args,**kwargs):,
#     把传入的参数和值打印出来。比如传入参数是
#     flexible(aa,2,3,x=4,y=5,*[1,2,3],**{'a':1,'b':2})
#     输出结果：（2,3,1,2,3）,{'a':1,'y':5,'b':2,'x':4}
#
def flexible(aa, *args, **kwargs):
    print(aa)
    print(args)
    print(kwargs)


flexible(2, 3, x=4, y=5, *[1, 2, 3], **{'a': 1, 'b': 2})

# 面试题:*args,**kwargs有什么作用
# 课程贴：18877
