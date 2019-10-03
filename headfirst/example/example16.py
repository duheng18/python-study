def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def coach_data(file_name, m=0, n=3):
    try:
        with open(file_name) as f:
            data = f.readline()
        item = data.strip().split(',')
        result = sorted(set([sanitize(t) for t in item]))[m:n]
        return result
    except IOError as err:
        print('File error:', str(err))
        return None


print(coach_data('james.txt'))
print(coach_data('julie.txt'))
print(coach_data('mikey.txt'))
print(coach_data('sarah.txt'))
