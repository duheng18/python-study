def add(x, *kwargs):
    total = x
    for param in kwargs:
        try:
            total += param
        except TypeError:
            pass
    print(total)


add(1, 2, 3, 'b', 4, 5)
