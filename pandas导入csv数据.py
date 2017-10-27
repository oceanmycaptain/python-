import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

#fig = plt.figure()
# ax1 = fig.add_subplot(2,2,1)#（2,2,1）指figure可以放4个图形，上下各两个的类型，后面的1指的指的是第一个。
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# #plt.plot([1.5,3.5,-2,1.6])
#ax = fig.add_subplot(1,1,1)#(1,1,1)指的是几个方阵，figure可以放1x1的一个，后面的1指第几个。
# plt.plot(randn(30).cumsum(),'go--')
# plt.xlim([0,30])
#plt.plot(randn(50).cumsum(),'k--')
# _ = ax1.hist(randn(100),bins=20,color='k',alpha=0.3)
# ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))
# plt.subplots_adjust(wspace=0,hspace=0)
# ax.plot(randn(1000).cumsum(),'r',label='one')
# ax.plot(randn(1000).cumsum(),'g--',label='two')
# ax.plot(randn(1000).cumsum(),'y.',label='three')
# ax.legend(loc='best')
# s = pd.Series(np.random.randn(10).cumsum(),index = np.arange(0,100,10))
# s.plot()
df = pd.DataFrame(np.random.randn(10,4).cumsum(0),columns = ['A','B','C','D'],index = np.arange(0,100,10))
df.plot()
plt.show()