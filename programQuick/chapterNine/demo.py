import shutil, os

os.chdir('C:\\')
# shutil.copy()将复制一个文件，shutil.copytree()将复制整个文件夹，以及它包含 的文件夹和文件。
shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
# 调用shutil.copytree(source, destination)，将路径source处的文件夹，包括它的所有文件和子文件夹，复制到路径 destination 处的文件夹。
# source 和 destination 参数都是字符串。该函数返回一个字符串，是新复制的文件夹的路径。
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

# 调用 shutil.move(source, destination)，将路径 source 处的文件夹移动到路径 destination，
# 并返回新位置的绝对路径的字符串。
shutil.move('C:\\bacon.txt', 'C:\\eggs')

for filename in os.listdir():
    if filename.endswith('.rxt'):
        # 调用 os.unlink(path)将删除 path 处的文件。
        # 调用 os.rmdir(path)将删除path处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹。
        # 调用 shutil.rmtree(path)将删除path处的文件夹，它包含的所有文件和文件夹都会被删除。
        os.unlink(filename)

# 利用send2trash，比 Python常规的删除函数要安全得多，因为它会将文件夹和文件发送到计算机的垃圾箱或回收站，
# 而不是永久删除它们。如果因程序缺陷而用 send2trash 删除了某些你不想删除的东西，稍后可以从垃圾箱恢复。
import send2trash

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
