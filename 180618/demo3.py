'''循环的扩展
循环与else
for <循环变量> in <遍历结构>:
        <语句块1>
else:
        <语句块2>

while <条件>:
        <语句块1>
else:
        <语句块2>
'''
s="PYTHON"
for c in s:
    if c=="T":
        continue
    print(c,end="")
else:
    print("正常退出")