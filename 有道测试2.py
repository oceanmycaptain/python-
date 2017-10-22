import urllib.request
import urllib.parse
import json
#这个代码完全是只是去掉translate_o才能运行出来，真不知道怎么回事，后面好好深入在细究。
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null"
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
data={}
data['i']='I love fishc.com'
#data['from']='AUTO'
#data['to']='AUTO'
#data['smartresult'] = 'dict'
#data['client'] = 'fanyideskweb'
data['salt'] = '1498463829573'
data['sign'] = 'f2297514612234fa169d71a5716963bd'
data['doctype'] = 'json'
#data['version'] = '2.1'
#data['keyfrom'] = 'fanyi.web'
#data['action'] = 'FY_BY_CLICKBUTTON'
#data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('UTF-8')
req=urllib.request.Request(url,data,head)

response = urllib.request.urlopen(req)

html = response.read().decode('UTF-8')

target=json.loads(html)
target=target['translateResult'][0][0]['tgt']

print(target)