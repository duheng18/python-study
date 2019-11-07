import os

path = '/Users/duheng/Documents/project/python/programQuick'
for folderName, subfolders, filenames in os.walk(path):
    # 1.当前文件夹名称的字符串。
    print('The current folder is ' + folderName)
    # 2.当前文件夹中子文件夹的字符串的列表。
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    # 3.当前文件夹中文件的字符串的列表。
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')