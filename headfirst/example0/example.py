class NameList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


johnny = NameList("John Paul Jones")
# <class '__main__.NameList'>
print(type(johnny))

print(dir(johnny))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
# '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__'
# , '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'name', 'pop', 'remove', 'reverse', 'sort']

johnny.append("Bass Player")
johnny.extend(['Composer', 'Arranger', 'Musician'])
# ['Bass Player', 'Composer', 'Arranger', 'Musician']
print(johnny)
# John Paul Jones
print(johnny.name)
for attr in johnny:
    # John Paul Jonesis aBass Player.
    # John Paul Jonesis aComposer.
    # John Paul Jonesis aArranger.
    # John Paul Jonesis aMusician.
    print(johnny.name + " is a " + attr + '.')
