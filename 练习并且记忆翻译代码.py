import urllib.request
import urllib.parse
import json

content = input('请输入想翻译的内容:')
url = ('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule')
head ={}
head['Referer'] ='http://fanyi.youdao.com'
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12088.400'
data ={}
data ['i'] = content#如果打算字符串会代码会直接翻译’content‘
data['from']= 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1506049812601'
data['sign'] ='4764142cb538ca901b44053343d2372d'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
trager = json.loads(html)
print('翻译的内容为：%s'%(trager['translateResult'][0][0]['tgt']))

