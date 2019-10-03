import pickle
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

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print(' File error: ', str(err))
except pickle.PickleError as perr:
    print('Pickling error:', str(perr))


def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print(each_item, indent, level + 1, fn)
        else:
            if indent:
                for tab_space in range(level):
                    print('\t', end='', file=fn)
            print(each_item, file=fn)


new_man = []
new_other = []
try:
    with open('man_data.txt', 'rb') as man_file, open('other_data.txt', 'rb') as other_file:
        new_man = pickle.load(man_file)
        new_other = pickle.load(other_file)
except IOError as err:
    print('File error:', str(err))
except pickle.PickleError as perr:
    print('Pickling error:', str(perr))
# print_lol(new_man)
print_lol(new_other)
# print(new_man[0])
print(new_other[-1])
