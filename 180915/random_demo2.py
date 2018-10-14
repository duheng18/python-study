values =  'Jack Queen'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
from pprint import pprint
for i in range(12):pprint(deck[:12])
from random import shuffle
shuffle(deck)
pprint(deck[:12])
