def collatz(number):
    try:
        if number % 2 == 0:
            result = number // 2
            print('result:',result)
            return result
        elif number % 2 == 1:
            result = 3 * number + 1
            print('result:',result)
            return result
        else:
            print('')
    except  TypeError:
        print('not number')
while True:
    print("Enter number:")
    try:
        number = int(input())
    except NameError as NE:
        print('except:',NE)
    except ValueError as VE:
        print('except:',VE)
    num=collatz(number)
    print("num:",num)
    if num == 1:
        break
