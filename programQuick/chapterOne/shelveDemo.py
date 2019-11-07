import shelve

shelveFile=shelve.open('mydata')
cats=['Zophie', 'Pooka', 'Simon']
shelveFile['cats']=cats
shelveFile.close()
shelfFile = shelve.open('mydata')
print(list(shelveFile.keys()))
print(list(shelveFile.values()))
shelveFile.close()