

with open('/Users/duheng/Documents/HeadFirstPython/chapter3/jamess.txt') as jaf:
    data=jaf.readline()
james=data.strip().split(',')
with open('/Users/duheng/Documents/HeadFirstPython/chapter3/julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')
with open('/Users/duheng/Documents/HeadFirstPython/chapter3/mikey.txt') as mif:
    data=mif.readline()
mikey=data.strip().split(',')
with open('/Users/duheng/Documents/HeadFirstPython/chapter3/sarah.txt') as saf:
    data=saf.readline()
sarah=data.strip().split(',')
print(james)
print(julie)
print(mikey)
print(sarah)
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
james.sort()
