import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    # Row #1 ['4/5/2014 13:34', 'Apples', '73']
    # Row #2 ['4/5/2014 3:41', 'Cherries', '85']
    # Row #3 ['4/6/2014 12:46', 'Pears', '14']
    # Row #4 ['4/8/2014 8:59', 'Oranges', '52']
    # Row #5 ['4/10/2014 2:07', 'Apples', '152']
    # Row #6 ['4/10/2014 18:10', 'Bananas', '23']
    # Row #7 ['4/10/2014 2:40', 'Strawberries', '98']
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
