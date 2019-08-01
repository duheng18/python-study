import os
import time

'''
查找/tomcat/log/目录下的log文件，如果文件最后修改时间是在1小时之前，把次文件打包压缩，
备份到/home/back/log目录下
os.system -linux打包命令
os.listdir()
os.stat()

'''
path = "/Users/duheng/Documents/project/python/190719/"
os.chdir("/Users/duheng/Documents/project/python/190719/")
for file in os.listdir(path):
    if file.endswith('.log'):
        var_mtime = os.stat(file).st_mtime
        var_nowtime = time.time()
        diff = var_nowtime - var_mtime
        if diff > 300:
            print(file)
    os.system("tar -zcvPf file /Users/duheng/Documents/project/python")
