try:
    data = open('its.txt', 'w')
    print("its...", file=data)
except IOError as err:
    print('File Error:' + str(err))
finally:
    if 'data' is locals():
        data.close()
