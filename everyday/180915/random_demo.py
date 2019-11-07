# random模块包括返回随机数的函数，可用于模拟或者用于任何产生随机输出的程序。
# random()返回0<n≤1之间的随机实数n
# getrandbits(n)以长整型形式返回n个随机位
# uniform(a,b)返回随机实数n，其中a≤n<b
# randrange(start,stop,step)返回range(start,stop,step)中的随机数
# choice（seq）从序列seq中返回随意元素
# shuffle(seq,random)原地指定序列seq，将给定序列的元素进行随机移位，每种排序的可能性都是近似相等的。
# sample(seq,n)从序列seq中选择n个随机且独立的元素。从给定序列中（均一地）选择给定数目的元素，同时确保元素互不相同。
from random import *
from time import *

date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
# 获取代表时间间隔限制的实数
time1 = mktime(date1)
print(time1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
print(time2)
random_time = uniform(time1, time2)
print(random_time)
print(localtime(random_time))
# time.struct_time(tm_year=2008, tm_mon=11, tm_mday=20, tm_hour=12, tm_min=20, tm_sec=5, tm_wday=3, tm_yday=325, tm_isdst=0)
print(asctime(localtime(random_time)))
# Fri Oct 24 17:10:58 2008
