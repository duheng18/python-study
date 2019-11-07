#! python3
# test:rjust,width


tableData=[['apples','oranges','cherries','banana'],
['Alice','Bob','Carol','David'],
['dogs','cats','moose','goose']]

def printTable(data):
    colwidths=[0]*len(data)
    for i in range(len(data)):
        col=[]
        for j in range(len(data[0])):
            col.append(len(data[i][j]))
            col.sort()
            colwidths[i]=col[-1]
            print(colwidths)

    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(colwidths[j]),end=' ')
        print()

printTable(tableData)
