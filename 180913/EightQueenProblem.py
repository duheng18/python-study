# 八皇后问题是一个以国际象棋为背景的问题：如何能够在8×8的国际象棋棋盘上放置八个皇后，
# 使得任何一个皇后都无法直接吃掉其他的皇后？为了达到此目的，任两个皇后都不能处于同一条横行、纵行或斜线上。
# 寻找冲突
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


# # 基本情况
# def queens(num, state):
#     if len(state) == num - 1:
#         for pos in range(num):
#             if not conflict(state, pos):
#                 yield pos
#     # print(list(queens(4, (1, 3, 0))))
#     # 需要递归的情况
#     else:
#         for pos in range(num):
#             if not conflict(state, pos):
#                 for result in queens(num, state + (pos,)):
#                     yield (pos,) + result
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


# print(list(queens(3)))
# print(list(queens(4)))
# for solution in queens(8):
#     print(solution)


# print(len(list(queens(8))))


# 打包
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '.' * (pos) + 'X' + "." * (length - pos - 1)

    for pos in solution:
        print(line(pos))


import random

prettyprint(random.choice(list(queens(8))))
