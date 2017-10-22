import requests
from bs4 import BeautifulSoup
import os
import re
global url_set urlname_set，
url_set = ['http://www.mzitu.com/98346']
global urlname_set
urlname_set = []
global urlimg_set
urlimg_set = []
global i
i= 1
def ope():
    res = requests.get(url_set[0])
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    soup_dic = soup.select('.main-image p a')
    url_set.append(soup_dic[0]['href'])
    soup_dic_1 = soup.select('.main-image img')
    urlimg_set.append(soup_dic_1[0]['src'])
    soup_dic_2 = soup.select('.main-image img')
    urlname_set.append(soup_dic_1[0]['alt'])
flag = 1
while flag != 100:
    ope()
    print (url_set)
    print (urlname_set)
    print (urlimg_set)
    if not(re.match('http://www.mzitu.com/\d*/\d*',url_set[0])):
        os.chdir(r'C:\Users\Administrator\Desktop\小黄图抓取简易版本')
        name = ''.join((str(urlname_set[0]).split('?')))
        os.mkdir(name)
        os.chdir(name)
    i = 1
    img = requests.get(urlimg_set[0])
    f = open(str(i)+'.jpg','ab')
    i = i+1
    f.write(img.content)
    f.close()
del url_set[0]
del urlname_set[0]
del urlimg_set[0]
flag = flag+1