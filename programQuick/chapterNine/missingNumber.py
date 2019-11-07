'''编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，诸如spam001.txt,spam002.txt 等，
并定位缺失的编号(例如存在 spam001.txt 和 spam003.txt，但不存 在 spam002.txt)。
让该程序对所有后面的文件改名，消除缺失的编号。作为附加的挑战，编写另一个程序，
在一些连续编号的文件中，空出一些编号， 以便加入新的文件。'''
import os,re,shutil
num = 1
for foldername,subfolders,filenames in os.walk('D:\\test9.2'):
    for filename in filenames:
        mo = re.compile(r'spam\d{3}.*(\.\w*)$').search(filename)
        if mo == None:
            continue
        else:
            if num < 10:
                temp = 'spam00'+str(num)+mo.group(1)
            if num>=10 and num<100:
                temp = 'spam0'+str(num)+mo.group(1)
            if num>=100:
                temp = 'spam'+str(num)+mo.group(1)
            print(temp)
            shutil.move(os.path.join(foldername,filename),os.path.join(foldername,temp))
            num=num+1