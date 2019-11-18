import datetime, time

# 2019-11-15 15:28:53.154418
# print(datetime.datetime.now())

dt = datetime.datetime(2019, 10, 21, 16, 29, 0)

# 2019 10 21
# print(dt.year, dt.month, dt.day)

# 16 29 0
# print(dt.hour, dt.minute, dt.second)

# 1970-01-12 21:46:40
# print(datetime.datetime.fromtimestamp(1000000))

# 2019-11-15 15:32:52.648261
# print(datetime.datetime.fromtimestamp(time.time()))

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
# True
print(halloween2015 == oct31_2015)
# False
print(halloween2015 > newyears2016)
# True
print(newyears2016 > halloween2015)
# True
print(newyears2016 != oct31_2015)
