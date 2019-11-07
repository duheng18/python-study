'''编写一个程序，遍历一个目录树，查找特定扩展名的文件(诸如.pdf 或.jpg)
不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。'''
import os, shutil

path = '/Users/duheng/Documents/project/python/programQuick/chapterNine'
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.pdf') or filename.endswith('.png'):
            print(os.path.join(foldername, filename))
            shutil.copy(os.path.join(foldername, filename), 'D:\\test9.1')
        else:
            continue
