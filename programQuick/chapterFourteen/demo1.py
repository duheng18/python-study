import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
# <class '_csv.reader'>
# print(type(exampleReader))
exampleData = list(exampleReader)
# [['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'],
# ['4/6/2014 12:46', 'Pears', '14'], ['4/8/2014 8:59', 'Oranges', '52'],
# ['4/10/2014 2:07', 'Apples', '152'], ['4/10/2014 18:10', 'Bananas', '23'],
# ['4/10/2014 2:40', 'Strawberries', '98']]
# print(exampleData)

# 4/5/2014 13:34
print(exampleData[0][0])

# Apples
print(exampleData[0][1])

# 73
print(exampleData[0][2])

# Cherries
print(exampleData[1][1])

# Strawberries
print(exampleData[6][1])
