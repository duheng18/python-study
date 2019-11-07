#一维数据的读入处理
#从空格分隔的文件中读入数据
#中国 美国 日本 德国 法国 英国 意大利
txt=open(fname).read()
ls=txt.split()
fname.close
