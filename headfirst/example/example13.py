min = [1, 2, 3]
secs = [m * 60 for m in min]
print(secs)

meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)

str = ["I", "don't", "like", "spam"]
lower = [s.lower() for s in str]
upper = [s.upper() for s in str]
print(lower)
print(upper)

with open('jamess.txt') as jaf: data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf: data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif: data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf: data = saf.readline()
sarah = data.strip().split(',')


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)

clean_0 = [float(s) for s in clean]
print(clean_0)

clean_1 = [float(sanitize(t)) for t in ["2-22", "3:33", "4.44"]]
print(clean_1)

print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))
