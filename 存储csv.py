import csv
import numpy as np
import pandas as pd

'''本次的目的是要生成一个CSV文档，有月份，有天数，有周几，有上午下午，还有那个车站，经过慎重考虑还是有numpy处理好'''
data1 = np.zeros([97356,6])
a =0
for i in range(9,11):
    for j in range(0,2):
        for k in range(0,2):
            for s in range(1,400):
                if i == 9:
                    for d in range(1,31):
                        data1[a][0] = i
                        data1[a][1] = d
                        data1[a][2] = j
                        data1[a][3] = k
                        data1[a][4] = s
                        a += 1
                if i == 10:
                    for d in range(1,32):
                        data1[a][0] = i
                        data1[a][1] = d
                        data1[a][2] = j
                        data1[a][3] = k
                        data1[a][4] = s
                        a += 1
n = 0
w =2
while n < len(data1):
    data1[n][5] = w
    n += 1
    w += 1
    if w == 8:
        w = 1
data2 = pd.DataFrame(data1)
data2.to_csv('data/九十月份.csv')

