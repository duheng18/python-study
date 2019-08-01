import time
from datetime import datetime
import sys

# print(sys.getdefaultencoding())


def time_format():
    print(time.time(), "1") #1970到现在的时间 时间是毫秒数
    print(time.localtime(), "2") #北京时间
    print(time.gmtime(), "3") #国际时间 差8小时
    print(time.strftime("%y/%m/%d %H:%M"), "4")
    print(time.strftime("%Y-%m-%d %H:%M:%S %Z"), "5")
    # print(sys.getdefaultencoding())
    # print(time.strftime("%Y-%m-%d %H:%M:%S %Z").decode(sys.getdefaultencoding()).encode("utf-8"))
    print(time.strftime("%c"), "6")
    time_tuple = time.strptime("1 Jan 2018 1:30pm", "%d %b %Y %I:%M%p")
    print(type(time_tuple), time_tuple)
    print("分割线", "**" * 20, "分割线")


def datetime_format():
    print(datetime.now())
    print(datetime.utcnow())
    print(datetime.now().strftime("%y/%m/%d %H:%M"))
    date_format = datetime.now().strptime("1 Jan 2018 1:30pm", "%d %b %Y %I:%M%p")
    print(type(date_format), date_format)


def time_delta():
    from datetime import datetime
    from datetime import timedelta
    d1 = datetime.strptime("2017-12-05 17:41:20", "%Y-%m-%d %H:%M:%S")
    d2 = datetime.strptime("2017-12-03 19:40:28", "%Y-%m-%d %H:%M:%S")
    delta = d2 - d1
    print(delta)

    # 后三天
    now = datetime.now()
    # print(now,"now")
    days_delta = timedelta(days=3)
    print(now + days_delta)

    hours_delta = timedelta(hours=0.5)
    print(now + hours_delta)

    mins_delta = timedelta(minutes=10)
    print(now + mins_delta)


if __name__ == "__main__":
    time_format()
    datetime_format()
    time_delta()

