# for循环语句
# for iterating in sequence:
#   statements(s)
# for 迭代出来的变量 in 要迭代的序列语句
from collections import Counter

# 凡是多个的都可以通过循环把每一个取出来，[1,100),'abcdefg',["apple","zip","banana","peach"]
for year in range(1,10):
    print("我活了"+str(year)+"年")

str1='abdkxjsl'
for i in str1:
    print('_'+i,end='')

lists=["apple","zip","banana","peach"]
for item in lists:
    print("我今天吃了"+item)

print(list(reversed(lists)))
print(list(sorted(lists)))

li=[x for x in range(10) if x % 2 == 0]
print(li)

lists2=lists*2
print(lists2)

my_counter=Counter(lists2)
print(my_counter.most_common())