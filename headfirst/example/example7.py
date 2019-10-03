try:
    with open('mis.txt') as data:
        print("it's...", file=data)
except IOError as err:
    print('File error:', str(err))
