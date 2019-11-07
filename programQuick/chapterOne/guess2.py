import random

secret = random.randint(1, 20)
print('secret:',secret)
for guesstime in range(1,7):
    print('Take a guess:')
    guess=int(input())
    if guess > secret:
        print('>')
    elif guess < secret:
        print('<')
    else:
        break
if guess == secret:
    print('==')
else:
    print('None')
