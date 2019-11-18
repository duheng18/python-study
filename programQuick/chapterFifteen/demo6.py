import datetime, time

'''
strftime 指令                     含义
    %Y                  带世纪的年份，例如'2014'
    %y                  不带世纪的年份，'00'至'99'(1970 至 2069)
    %m                  数字表示的月份, '01'至'12'
    %B                  完整的月份，例如'November'
    %b                  简写的月份，例如'Nov'
    %d                  一月中的第几天，'01'至'31'
    %j                  一年中的第几天，'001'至'366'
    %w                  一周中的第几天，'0'(周日)至'6'(周六)
    %A                  完整的周几，例如'Monday'
    %a                  简写的周几，例如'Mon'
    %H                  小时(24 小时时钟)，'00'至'23'
    %I                  小时(12 小时时钟)，'01'至'12'
    %M                  分，'00'至'59'
    %S                  秒，'00'至'59'
    %p                  'AM'或'PM'
    %%                  就是'%'字符
'''

halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
# 2015/10/21 16:29:00
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))

# 04:29 PM
# print(oct21st.strftime('%I:%M %p'))

# October of '15
print(oct21st.strftime("%B of '%y"))

# 2015-10-21 00:00:00
# print(datetime.datetime.strptime('October 21,2015', '%B %d,%Y'))
# 2015-10-21 16:29:00
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))

# 2015-10-01 00:00:00
# print(datetime.datetime.strptime("October of '15", "%B of '%y"))

# 2063-11-01 00:00:00
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))
