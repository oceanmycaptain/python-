import urllib.request
import re
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    page =urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html
def get_img(html):
    p = r'<img id="Image".+?"(.+?)".+?>'#正则表达式有点糊涂，关于.+?的相关方面
    #该正则表达式是以(")来进行我们想要的匹配数据的，用括号可以直接匹配我们想要的数据，并且来运用我们的数据。
    imglist = re.findall(p,html)
    #(<img id="image" src="http://jiangsu.china.com.cn/uploadfile/2016/0510/1462846638673201.jpg" )

    for each in imglist:
        print(each)
    #x = 0
    # for each in imglist:
    #     filename = each.split('/')[-1]
    #     #此时我们以“/”来做为我们切割对象，会成为几个列表，我们需要的只是带有.jpg这部分，所以我们得切片将他单独提取下来是最后一个位置[6]也是倒数第一个位置[-1]
    #     a = 'e:\爬下的文件\%s.jpg'%x
    #     #指定我们下载的位置
    #     urllib.request.urlretrieve(each,a,None)
    #     #print(filename)
    #     x = x+1

if __name__ == '__main__':
    url = 'http://jiangsu.china.com.cn/uploadfile/2016/0510/1462846638673201.jpg'
    get_img(open_url(url))