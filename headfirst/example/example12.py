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
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []
# for each_item in james:
#     clean_james.append(sanitize(each_item))
clean_james = [sanitize(each_t) for each_t in james]
# for each_item in julie:
#     clean_julie.append(sanitize(each_item))
clean_julie = [sanitize(each_t) for each_t in julie]
# for each_item in mikey:
#     clean_mikey.append(sanitize(each_item))
clean_mikey = [sanitize(each_t) for each_t in mikey]
# for each_item in sarah:
#     clean_sarah.append(sanitize(each_item))
clean_sarah = [sanitize(each_t) for each_t in sarah]

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
