try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError as error:
    print('File Error:', str(error))
finally:
    if 'data' is locals():
        data.close()
