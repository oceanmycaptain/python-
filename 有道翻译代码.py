import urllib.request
import urllib.parse
import time
import random
import hashlib
import json
#此个代码完全就是拥有解码的密钥才可以爬下有道翻译。
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'


def open_url(url, word_d):
    u = 'fanyideskweb'
    d = word_d
    f = str(int(time.time() * 1000))#此处是给解码了？
    c = "rY0D^0'nM0}g5Mm1z%1G4"
    g = hashlib.md5()
    g.update((u + d + f + c).encode('utf-8'))
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'
    head['Host'] = 'fanyi.youdao.com'
    head['Referer'] = 'http://fanyi.youdao.com/'
    data = {}
    data['i'] = d
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = u#这三个是有道翻译密匙的关键（‘client，salt，sign’）
    data['salt'] = f
    data['sign'] = g.hexdigest()
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CL1CKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    #print(html)
    print('翻译结果： %s ' % (target['translateResult'][0][0]['tgt']))


def loops(url):
    while True:
        d = input('请输入需要翻译的单词或句子（‘99’表示退出）：')
        if d == '99':
            break
        else:
            open_url(url, d)


if __name__ == '__main__':
     url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
     loops(url)
