# somescript.py
import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)

# cat somefile.txt:将文件somefile.txt的内容写入到标准输出(sys.stdout)。
# python somescript.py:执行Python脚本somescript。这个脚本从其标准输入中读取，并将结果写入到标准输出。
#  cat somefile.txt | python somescript.py
# ('Wordcount:', 11)


