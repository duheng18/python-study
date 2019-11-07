values1 = range(1, 12)
values2 = 'Jack Queen'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values1 for s in suits]
from pprint import pprint
# for i in range(12):pprint(deck[:12])
from random import shuffle

shuffle(deck)
pprint(deck[:12])
# 每次按回车的时候都发一张牌，直到发完为止。
while deck: input(deck.pop())
