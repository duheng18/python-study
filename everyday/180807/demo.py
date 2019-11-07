import jieba
import wordcloud

f=open("新时代中国特色社会主义.txt","r",encoding="UTF-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
path="//Library//Fonts//Songti.ttc"
w=wordcloud.WordCloud(font_path=path,width=1000,height=700,background_color="white",max_words=15)
w.generate(txt)
w.to_file("maxcloud.png")