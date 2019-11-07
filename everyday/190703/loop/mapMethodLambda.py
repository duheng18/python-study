def f(s):
    return s[0:1].upper() + s[1:].lower()


list1 = ['lll', 'lKK', 'wXy']
a = map(f, list1)
print(a)
print(list(a))
