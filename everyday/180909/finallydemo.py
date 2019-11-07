# finally
x = None
try:
    x = 1 / 0
except:
    print('something')
finally:
    print('Cleaning up ...')
    del x

try:
    1 / 0
except:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")
