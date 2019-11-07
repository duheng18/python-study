'''

编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达 式的所有行。结果应该打印到屏幕上。
'''
import re
import os

folderPath = input('Please input the FolderPath:')
fileNameList = os.listdir(folderPath)
for filename in fileNameList:
    mo = re.compile(r'.+\.txt$')
    file = mo.search(filename)
    if file == None:
        continue
    else:
        fileContentTxt = open(os.path.join(folderPath, file.group())).read()
        matchRegEx = re.compile(r'import').findall(fileContentTxt)
        print('\n'.join(matchRegEx))
