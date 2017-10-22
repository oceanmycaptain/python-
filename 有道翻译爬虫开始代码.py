import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容:')
#url = ("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link")
url = ('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule')
head = {}#模拟浏览器的访问头
head['Referer'] = 'http://fanyi.youdao.com'
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1500905968164'
data['sign'] = '27835850cdbe839dcb252526f3d6ac0b'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CL1CKBUTTON'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')#将data转码

req = urllib.request.Request(url, data, head)#用自己设定的访问头和数据去模拟访问我们想访问的网址
response = urllib.request.urlopen(req)#访问后抓取并且打开我们想访问的网址
html = response.read().decode('utf-8')#读取后将我们读取的信息进行转码操作
target = json.loads(html)#装载我们的信息
#print('翻译结果： %s' % (target['translateResult'][0][0]['tgt']))
print('翻译结果:%s'%(target['translateResult'][0][0]['tgt']))