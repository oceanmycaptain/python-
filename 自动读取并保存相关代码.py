import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

txt_data = open('C:/Users/a/Desktop/123.txt','r')
data1 =eval(txt_data.readline())
a = {}
key2 = {}
for key in data1:#这整个一步骤都是为了将日期标准化，和
    key1 = datetime.datetime.strptime(key, '%Y/%m/%d')
    key2 = datetime.datetime.strftime(key1, '%Y-%m-%d')
    a[key2] = data1[key]

#for n in range(1,400):#听说xrange在大数据运行时，效率不错，等一下可以考虑这块，它针对的不是list格式的。
n = 122
while n<400:
    data = np.load('./chewei/%s.npy'%n)#打开一个文件夹的同一类型的所有文件。

    for i in range(0,4):
        a0_value = list(data[i])#

        a_key2 = list(a.keys())
        a_value = list(a.values())
        a0 =dict(zip(a_key2,a0_value))#让两个列表自动形成字典相互对应。

        df = pd.Series(a0)
        plt.rc('figure',figsize =(30,15))#进行储存的图片的内容调节
        df.plot(kind='bar')#此时为了画柱状图
        fig = plt.gcf()#如果没有这一步会出现，下载的图片的空白
        #plt.show()
        fig.savefig('C:/Users/a/Desktop/cycle1/%d号车位%d.png'%(n,i),pdi=1000,bbox_inches='tight')
        # 存于我们想要放的地方，进行不同命名储存。
        plt.close()
        #如果我们不主动关闭，它就会默认等待十秒关闭。
    n += 1
