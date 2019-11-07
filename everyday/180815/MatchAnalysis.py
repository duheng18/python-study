from random import *


# 打印程序的介绍性信息
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示)")


# 获取程序运行参数probA,proB
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1):"))
    b = eval(input("请输入选手B的能力值(0-1):"))
    n = eval(input("模拟比赛的场次："))
    return a, b, n


# 输出球员AB获胜比赛的场次及概率
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))


def gameOver(a, b):
    return a == 15 or b == 15


# 模拟一局比赛
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


# 利用球员A和B的能力值，模拟n局比赛
# 模拟n局比赛，相当于n次模拟一局比赛
def simNGames(n, probA, probB):
    #设定AB获胜的场次变量
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


main()
