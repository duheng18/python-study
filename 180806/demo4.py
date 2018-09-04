import jieba
import wordcloud

txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它安按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理"
w = wordcloud.WordCloud(width=1000, font_path="//Library//Fonts//Songti.ttc", height=700)
# jieba中文分词库 jieba.lcut将这段文件进行分词 lcut会生成一个列表变量，其中的每一个元素是分隔之后的单词。
# 然后让这样的单词以文本的形式由空格来分隔组成。我们可以使用" ".join函数将这样的列表由空格将各个元素组织起来。
w.generate(" ".join(jieba.lcut(txt)))
# 中文需要先分词并组成空格分隔字符串
w.to_file("pywcloud.png")
