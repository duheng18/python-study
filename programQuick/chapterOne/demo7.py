
helloFile=open('/Users/duheng/Documents/project/python/programQuick/chapterOne/hello.txt')
helloContent=helloFile.read()
# print(helloContent)

someFile=open('sonnet29.txt')

someContent1=someFile.readlines()
# print(someContent1)
# someContent=someFile.read()
# print(someContent)

bacoFile=open('bacon.txt','w')
print(bacoFile.write('Hello world!\n'))
bacoFile.close()
bacoFile=open('bacon.txt','a')
print(bacoFile.write('Bacon is not a vegetable.'))
bacoFile.close()
bacoFile=open('bacon.txt')
content=bacoFile.read()
bacoFile.close()
print(content)