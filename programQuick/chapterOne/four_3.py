def listsortstr(temp):
    str=''
    for m in temp[:-1]:
        print(m)
        str+=m+', '
    return str+'and'+' '+temp[-1]
spam=['apples','bananas','tofu','cats']
print(listsortstr(spam))