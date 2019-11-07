import os

# usr/bin/spam
print(os.path.join('usr', 'bin', 'spam'))
# myFile=['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFile:
#     print(os.path.join('/Users/duheng',filename))
# print(os.getcwd())
# print(os.path.abspath('.'))
# print(os.path.relpath('C:\\Windows', 'C:\\'))
# print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
# print(os.getcwd())
name = 'C://Windows/System32/calc.exe'
# C://Windows/System32
print(os.getcwd())
print(os.path.dirname(name))
# calc.exe
print(os.path.basename(name))
# ('C://Windows/System32', 'calc.exe')
print(os.path.split(name))
# ['C:', '', 'Windows', 'System32', 'calc.exe']
print(name.split(os.path.sep))
# ['', 'usr', 'bin']
print('/usr/bin'.split(os.path.sep))
print(os.path.getsize('.'))
totalSize = 0
dir = '/Users/duheng/Documents/project/python/programQuick/chapterOne'
for filename in os.listdir(dir):
    totalSize = totalSize + os.path.getsize(os.path.join(dir, filename))
print(totalSize)
print(os.path.exists('C://Windows/System32'))
print(os.path.isdir('/Users/duheng/Documents/project/python/programQuick/chapterOne'))
print(os.path.isfile('/Users/duheng/Documents/project/python/programQuick/chapterOne/demo.txt.py'))
