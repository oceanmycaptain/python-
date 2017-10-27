import numpy as np
import pylab as pl
import pandas as pd
import json
import matplotlib.pyplot as plt
import datetime

data = open('C:/Users/a/Desktop/123.txt','r')
data1 =eval(data.readline())
#print(type(data1))
data2 = {}
for key in data1:
    key1=datetime.datetime.strptime(key,'%Y/%m/%d')#此次的是将时间日期变为可比较化
    key2=datetime.datetime.strftime(key1,'%Y-%m-%d')
     # '''此次我又将时间给字符化，因为上一次的转化，我的不标准格式已经全部被标准化了，但是上次他将时间都精确到秒分来，
      # 不适应画图，故此次重新转化。 '''
    data2[key2] = data1[key]#此时将我们改变的key值对应的value重新映射回来。
df = pd.Series(data2)
print(df)
df.plot(kind = 'bar')#直方图
plt.show()

#collect[b][0]=datetime.datetime.strptime(collect[b][0],'%Y:%M:%D')
#data1.plot(data1)
#data1 = data.readline()
#with data as myfile:
#     data1 = myfile.read()
#dict = ast.literal_eval(data1)
#dict = eval(data1)#一直想不通之前为什么会无法转换成dict格式，最后发现用eval可以完美解决。
#print(dict)
#开始将数据序列化


