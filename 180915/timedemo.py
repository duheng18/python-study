# time模块包含的函数可以实现以下功能：获得当前时间、操作时间和日期、从字符串读取时间以及格式化时间为字符串。
# python日期元组的字段含义
# 序号	字段	值
# 0	4位数年	2008
# 1	月	1 到 12
# 2	日	1到31
# 3	小时	0到23
# 4	分钟	0到59
# 5	秒	0到61 (60或61 是闰秒)
# 6	一周的第几日	0到6 (0是周一)
# 7	一年的第几日	1到366 (儒略历)
# 8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
import time

# asctime([tuple])将时间元组转换为字符串
# time.asctime(时间元组)，默认为当前时间
print(time.asctime())
# Mon Oct  8 23:34:55 2018

# loaltime([secs])将秒数转换为本地时间的日期元组。如果想获得全球统一时间，则可以使用gmtime.
print(time.localtime(time.time()))
# time.struct_time(tm_year=2018, tm_mon=10, tm_mday=8, tm_hour=23, tm_min=36, tm_sec=8, tm_wday=0, tm_yday=281, tm_isdst=0)

# mktime(tuple)将日期元组转换为本地时间
# （4）时间元组 → 时间戳
# 1539092310.1404312
time.mktime((2018, 10, 9, 21, 38, 10, 6, 273, 0))

# sleep(secs)休眠，让解释器等待给定的秒数

# strptime(string,format) 将字符串解析为时间元组
# （6）时间元组 → 可视化时间（定制）
# time.strftime(要转换成的格式，时间元组)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 2018-10-09 22:05:19

# time()当前时间
print(time.time())
# 1539093919.751929
# 支持日期和时间的算法：datime ;帮助开发人员对代码段的执行时间进行计时：timeit
