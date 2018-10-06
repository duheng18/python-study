# encoding:utf-8
# fileinput模块能够轻松地遍历文本文件的所有行。
# fileinput.input(files,inplace,backup)便于遍历多个输入流中的行。
# fileinput.filename()返回当前文件的名称
# fileinput.lineno()返回当前（累计）的行数。在完成一个文件的处理并且开始处理下一个文件的时候，行数并不会重置，
# 而是将上一个文件的最后行数加1作为计数的起始。
# fileinput.filelineno()返回当前处理文件的当前行数。每次处理完一个文件并且开始处理下一个文件时，
# 行数都会重置为1，然后重新开始计数。
# fileinput.isfirstline()检查当前行是否是文件的第一行，如果是返回真值，反之返回假值。
# fileinput.isstdin()检查最后一行是否来自sys.stdin
# fileinput.nextfile()关闭当前文件，跳到下一个文件，跳过的行并不计。
# fileinput.close()关闭序列
# files:文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]
# inplace: 是否将标准输出的结果写回文件，默认不取代
# backup:备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
# bufsize:冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
# mode:读写模式，默认为只读
# openhook:该钩子用于控制打开的所有文件，比如说编码方式等;
# numberlines.py

import fileinput
import sys

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print('%-40s # %2i' % (line, num))


