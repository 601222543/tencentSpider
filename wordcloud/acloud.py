# coding: utf-8

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
# from matplotlib.image import imread
import jieba
from wordcloud import WordCloud, ImageColorGenerator

# 获取当前文件路径
d = path.dirname(__file__)

back_coloring_path = "article.png"  # 设置背景图片路径
text_path = 'dongguan.txt'  # 设置要分析的文本路径
font_path = 'C:\\Windows\\Fonts\\SIMHEI.TTF'  # 为matplotlib设置中文字体路径
back_coloring = imread(path.join(d, back_coloring_path))  # 设置背景图片
# back_coloring = plt.imread(path.join(d, back_coloring_path))

# 设置词云属性
wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=100,  # 字体最大值
               width=1000, height=860,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存
               margin=2,  # margin为词语边缘距离
               )

text = open(path.join(d, text_path), encoding='utf-8').read()


def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)
    for myword in liststr.split('/'):
        if len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

text = jiebaclearText(text)

# 生成词云, 可以用generate输入全部文本
wc.generate(text)
image_colors = ImageColorGenerator(back_coloring)

# 绘制词云
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()

