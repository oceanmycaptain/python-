import urllib.request
import re
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    page =urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html
def get_img(html):
    #p = r'<img class="BDE_Image".+?"(.+?)".+?>'#正则表达式有点糊涂，关于.+?的相关方面
    p = r'<img class="BDE_Image".+?"(.+?").+?">'
    #我们从网页上爬下的连接为
    #<img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=a213f8a92f381f309e198da199004c67/c950352ac65c10386f7f0453b5119313b07e891a.jpg" size="36374" width="479" height="852">
    imglist = re.findall(p,html)

    for each in imglist:
        print(each)

    # for each in imglist:
    #     filename = each.split('/')[-1]
    #    # urllib.request.urlretrieve(each,filename,None)

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/5341607680'
    get_img(open_url(url))