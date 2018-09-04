#DayDayUpQ4.py

def dayUP(df):
    dayup=1
    for i in range(365):
        if i%7 in [0,6]:
            dayup = dayup*(1-0.01)
            print("下降：{:.3f}".format(dayup))
        else:
            dayup = dayup*(1+df)
            print("向上：{:.3f}".format(dayup))
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
          dayfactor+=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
