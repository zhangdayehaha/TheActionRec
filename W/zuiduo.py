#coding:utf-8
import jieba
from collections import Counter
import json
import matplotlib.pyplot as plt
import matplotlib
import sys
filename="2020-03-06"
def tongji(filename):
    
    #解决matplotlib显示中文乱码的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family']='sans-serif'
    try:
        xianni=open(filename+".txt",'r',encoding='utf-8').read()
    except:
        xianni=open(filename+".txt",'r',encoding='gbk').read()
    xianni_words = [x for x in jieba.cut(xianni) if len(x) >= 6] #将全文分割，并将大于两个字的词语放入列表
    c=Counter(xianni_words).most_common(10) #取最多的10组
    print (json.dumps(c, ensure_ascii=False))

    name_list=[x[0] for x in c] #X轴的值
    num_list=[x[1] for x in c] #Y轴的值
    b=plt.bar(range(len(num_list)), num_list,tick_label=name_list)#画图

    plt.xlabel(u'词语')
    plt.ylabel(u'次数')
    plt.title(u'文本分词统计')
    plt.show()#展示
    #https://www.jianshu.com/p/a29f42690621
tongji(filename)
