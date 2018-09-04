cout=0
def hanoi(n,src,dst,mid):
    global cout
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
        cout+=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        cout+=1
        hanoi(n-1,mid,dst,src)
hanoi(3,"A","C","B")
print(cout)