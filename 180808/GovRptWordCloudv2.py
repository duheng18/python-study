import jieba
import wordcloud
from scipy.misc import imread

f=open("//Users//baidu//Downloads//tescase//python//180807//新时代中国特色社会主义.txt","r",encoding="UTF-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
mask0=imread("chinamap.jpeg")
path="/Library//Fonts//Songti.ttc"
w=wordcloud.WordCloud(font_path=path,mask=mask0,width=1000,height=700,background_color="white")
w.generate(txt)
w.to_file("mapcloud.png")