#!/usr/bin/env python
#coding=utf=8

for i in range (1,21):
    if i%3==0 and i%5==0:
        print("threes+fives")
    elif i%3==0:
        print("threes")
    elif i%5==0:
        print("five")
    else:
        print(i)
        continue
