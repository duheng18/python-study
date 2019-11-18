import time, datetime

startTime = datetime.datetime(2019, 11, 15, 19, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)
print('Program now starting on Halloween 2029')
