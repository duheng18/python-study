def func1(li):
    for item in li:
        str = item + ', '
        if li.index(item) == len(li) - 1:
            str = 'and ' + item
        print(str, end='')


spam = ['apple', 'bananas', 'tofu', 'cats']
func1(spam)
