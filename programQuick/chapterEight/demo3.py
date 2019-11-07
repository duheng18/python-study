import os

path='/Users/duheng/Documents/project/python/programQuick/chapterEight'
for filename in os.listdir(path):
    if filename.endswith('.rxt'):
        print(filename)
        os.unlink(filename)
