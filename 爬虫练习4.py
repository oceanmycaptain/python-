import requests
from bs4 import BeautifulSoup
import bs4
import os
import time

def qishibaike():
    num  = 0
    f = open('E:/下载文件/11.txt','w',encoding='utf-8')
    os.system('del*.jpg')
    request = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(request,'html.parser')
    main_field = soup.find('div',id = 'content-left')
    #找到我们想要的信息在那一块
    for joke_block in main_field.children:
        #找到main_field的子类可以用children
        if type(joke_block) == bs4.element.Tag and joke_block.name == 'div':
            #再次细分找到我们想要的类型
            num = num + 1
            author = joke_block.find('h2').get_text(strip=True)
            #爬下我们的爬下的作者的名字Id
            joke_content = joke_block.find('div',class_='content').get_text(strip = True)
            #爬下我们爬的文章
            f.write('------------\n')
            #用该符号来开头
            f.write('{0}'.format(num) + author)
            f.write('\n')
            f.write(joke_content)
            #写下我们的爬的文章
            f.write('\n')
            pic_tag = joke_block.find('div',class_='thumb')
            #找到图片的地点
            if pic_tag != None:
                #接下来爬我们的在此网站爬的图片
                pic_link = pic_tag.find('img').get('src')
                pic_request = requests.get('http:'+pic_link)
                with open('E:/下载文件/{0}.jpg'.format(num),'wb') as file:
                    #打开个我们的文件
                    file.write(pic_request.content)
    f.close()

if __name__ == '__main__':
    while(1):
        qishibaike()
        print(time.asctime(time.localtime(time.time())))
        time.sleep(30)
        #该处设置一个循环的时间，防止下载过快避免被封的ip


