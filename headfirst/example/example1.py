man=[]
other=[]
try:
    data=open('/Users/duheng/Documents/HeadFirstPython/chapter3/sketch.txt','r',encoding='utf-8')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The dat file is missing!')
print(man)
print(other)
