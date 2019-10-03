import sys

man = []
other = []
try:
    data = open('/Users/duheng/Documents/HeadFirstPython/chapter3/sketch.txt', 'r', encoding='utf-8')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')


# try:
#     with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
#         print(man, file=man_file)
#         print(other, file=other_file)
# except IOError as err:
#     print('File error:', str(err))


def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print(each_item, indent, level + 1, fn)
        else:
            if indent:
                for tab_space in range(level):
                    print('\t', end='', file=fn)
            print(each_item, file=fn)


print_lol(man)
