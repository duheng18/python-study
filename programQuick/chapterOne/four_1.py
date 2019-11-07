def func(spam):
    str=''
    for i in range(len(spam)-1):
        str=str+spam[i]+', '
    str=str+'and '
    str=str+spam[len(spam)-1]
    return str

spam=['apple','bananas','tofu','cats']
print(func(spam))

