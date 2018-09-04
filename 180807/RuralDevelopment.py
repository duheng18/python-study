import jieba
import wordcloud

f=open("关于实施乡村振兴战略的意见.txt","r",encoding="UTF-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
path="//Library//Fonts//Songti.ttc"
w=wordcloud.WordCloud(font_path=path,width=1000,height=700,background_color="white",max_words=15)
w.generate(txt)
w.to_file("countrycloud.png")