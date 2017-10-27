import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import datetime

data = open('C:/Users/a/Desktop/123.txt','r')
data1 =eval(data.readline())
a = {}
for key in data1:

    key1=datetime.datetime.strptime(key,'%Y/%m/%d')
    key2=datetime.datetime.strftime(key1,'%Y-%m-%d')
    a[key2] = data1[key]
df = pd.Series(a)
df.plot(kind = 'bar')
plot.show()




# #collect[b][0]=datetime.datetime.strptime(collect[b][0],'%Y:%M:%D')
#print(a)
