import csv
import os
import os.path
import codecs


fname = 'C:/Users/a/Desktop/cycle'
for file in os.walk(fname):
    #print(file)
    c ={}
    for a in file[2]:
        f = open('C:/Users/a/Desktop/cycle/'+a)
        b = len(list(f))-1
        c[a] =  b
    print(c)

file1 = open('C:/Users/a/Desktop/234.txt','w')
file1.write(str(c))
file1.close()
