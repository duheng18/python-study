gride = [['.', '.', '.', '.', '.', '.'],
         ['.', '0', '0', '.', '.', '.'],
         ['0', '0', '0', '0', '.', '.'],
         ['0', '0', '0', '0', '0', '.'],
         ['.', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '.'],
         ['0', '0', '0', '0', '.', '.'],
         ['.', '0', '0', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]


def func(list):
    g = len(list)
    c = len(list[0])
    for j in range(c):
        if j < c:
            for i in range(g):
                if i < g:
                    print(list[i][j], end=' ')
                    i = i + 1
        print('\n')
        j = j + 1


func(gride)
