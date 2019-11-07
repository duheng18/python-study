import zipfile, os

newZip = zipfile.ZipFile('example.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# path='/Users/duheng/Documents/project/python/programQuick/chapterNine'
# os.chdir(path)

# 要创建一个 ZipFile 对象，就调用 zipfile.ZipFile()函数，向它传入一个字符串，表示.zip 文件的文件名。
exampleZip = zipfile.ZipFile('example.zip')
# ZipFile 对象有一个namelist()方法，返回ZIP文件中包含的所有文件和文件夹的字符串的列表。
print(exampleZip.namelist())
# 这些字符串可以传递给ZipFile对象的getinfo()方法，返回一个关于特定文件的ZipInfo对象。
spamInfo = exampleZip.getinfo('spam.txt')
# ZipInfo 对象有自己的属性，诸如表示字节数的 file_size 和 compress_size，
# 它们分别表示原来文件大小和压缩后文件大小。ZipFile 对象表示 整个归档文件，
# 而 ZipInfo 对象则保存该归档文件中每个文件的有用信息。
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()

exampleZip=zipfile.ZipFile('example.zip')
exampleZip.extractall('/Users/duheng/Documents/project/python/programQuick/chapterNine/demo')