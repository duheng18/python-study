ls=[[1,2,3],[3,4,5],[6,7,8]] #二维列表
fname="a.csv"
f=open(fname,'w')
for item in ls:
    f.write(','.join('%s' %id for id in item)+'\n')
f.close
