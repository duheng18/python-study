fname="a.csv"
fo=open(fname)
ls=[]
for line in fo:
    line=line.replace("\n","")
    ls.append(line.split(","))
fo.close()
print(ls)
