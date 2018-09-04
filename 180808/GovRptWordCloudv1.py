import jieba
import wordcloud
from scipy.misc import imread

mamask = imread("fivestart.png")
f = open("//Users//baidu//Downloads//tescase//python//180807//关于实施乡村振兴战略的意见.txt", "r", encoding="UTF-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
path = "//Library//Fonts//Songti.ttc"
w = wordcloud.WordCloud(font_path=path, mask=mamask, \
                        width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("maskcloud.png")
