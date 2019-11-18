import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# 11 36548 0
# print(delta.days, delta.seconds, delta.microseconds)
# 986948.0
# print(delta.total_seconds())
# 11 days, 10:09:08
# print(str(delta))

dt = datetime.datetime.now()
# 2019-11-15 15:53:10.197490
# print(dt)

thousandDays = datetime.timedelta(days=1000)
# 2022-08-11 15:58:36.556213
# print(dt+thousandDays)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
# 2015-10-21 16:29:00
print(oct21st)
# 1985-10-28 16:29:00
print(oct21st - aboutThirtyYears)
# 1955-11-05 16:29:00
print(oct21st - (2 * aboutThirtyYears))
