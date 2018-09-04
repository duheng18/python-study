'''s="PYTHON"
for c in s:
    if c =="T":
        continue
    print(c,end="")
else:
    print("\n退出程序")
    '''
s="PYTHON"
for c in s:
    if c=="T":
        break
    print(c,end="")
else:
    print("\n退出程序")