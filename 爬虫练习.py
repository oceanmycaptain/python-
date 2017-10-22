#coding = utf-8
#urllib模块提供了读取web页面数据的接口
import urllib.request
import socket
import re
import sys
import os
targetDir = r'F:python下载处'#设置下载地点F盘
def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir,path[pos+1:])
    return t
if __name__ == '__main__':#程序运行的入口
    b = 'https://www.douban.com/'
    #a = urllib.request.urlopen( 'https://www.douban.com/')
    aheader2 = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Connection':'keep-alive'}
    #构造请求头
    aheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12088.400'}
    req = urllib.request.Request(url = b, headers = aheader2)
    #此处是用来干什么的？访问时可以将headers改成我们想要的用户名。发送请求头
    a = urllib.request.urlopen(req)#发送请求报头
    data = a.read()
    for link, t in set(re.findall(r'(http:[^s]*?(jpg|png|gif))',str(a))):
        print(link)
        try:
            urllib.request.urlretrieve(link,destFile(link))#下载图片
        except:
            print('失败')#异常抛出
        #data = data.decode('utf-8')
    # print(data)
