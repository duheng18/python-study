def coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as err:
        print('File error:', str(err))
        return None


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def get_sort(file_name):
    item = coach_data(file_name)
    result = sorted([sanitize(t) for t in item])

    return result


print(get_sort('james.txt'))
print(get_sort('julie.txt'))
print(get_sort('mikey.txt'))
print(get_sort('sarah.txt'))
