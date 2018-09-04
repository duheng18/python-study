score =  eval(input())
if 0<score<=60:
    grade='E'
elif 60<score<=70:
    grade='D'
elif 70<score<=80:
    grade = 'C'
elif 80<score<=90:
    grade = 'B'
else:
    grade='A'
print("我的成绩是{}".format(grade))