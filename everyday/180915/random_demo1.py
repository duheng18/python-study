from random import randrange

num = eval(input('How many dice?'))
sides = eval(input('How many sides per die?'))
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print('The result is', num)
