def flexible(aa,*args,**kwargs):
    list1=[]
    dic1={}
    for parm in args:
        list1.append(parm)
    print(list1)
    for k,v in kwargs.items():
        dic1.update(**kwargs)
    print(dic1)

flexible("aa", 2, 3, x=4, y=5, *[1, 2, 3], **{'a': 1, 'b': 2})