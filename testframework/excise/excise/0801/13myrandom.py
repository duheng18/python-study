# 测试常用内置函数
# Random：随机，测试多用于生成测试数据与测试报告文件的全名等
# time：时间，测试多用于处理时间等等，测试报告带时间的格式输出等
# Os：对操作系统进行的操作
# Sys：系统相关信息
# Re：正则
# subprocess：进程，执行操作系统的命令
# Logging：日志
import time
import os

# 生成的测试报告的名字是根据当前时间和文件名全名的。
report_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
print(time.localtime())
print(report_time + "_" + os.path.basename(__file__))

import random
import string

# 将序列中的某个随机取出来作为测试数据。序列可以是列表、字符串等
courses = ['python', 'java', 'selenium', 'Appium']
random_course = random.choice(courses)
print(random_course)

# 大写小写字母和数字随机拼接为测试数据
print(string.ascii_lowercase + "  " + string.ascii_uppercase + " " + string.digits)
rad_str = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
print(rad_str + "@163.com")
os.path.exists()
