import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容:')
#url = ("http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link")
url = ('http://fanyi.youdao.com/translat)?smartresult=dict&smartresult=rule')#一直不明白去掉'_o'居然就能成功爬下来的原因。
# head = {}
# head['Referer'] = 'http://fanyi.youdao.com'
#head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# data = {
#     "type": "AUTO",
#     "i": content,
#     "doctype": "json",
#     "xmlVersion": "1.8",
#     "keyfrom": "fanyi.web",
#     "ue": "UTF-8",
#     "action": "FY_BY_CLICKBUTTON",
#     "typoResult": "true"
# }
data = {
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1500092479607',
    'sign': 'c98235a85b213d482b8e65f6b1065e26',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CL1CKBUTTON',
    'typoResult': 'true'}
data['i'] = content
# data = {}
# data['i'] = content
# data['from'] = 'AUTO'
# data['to'] = 'AUTO'
# data['smartresult'] = 'dict'
# data['client'] = 'fanyideskweb'
# data['salt'] = '1505974296474'
# data['sign'] = '913822891b063cc2b7cac3180b772093'
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] = 'fanyi.web'
# data['action'] = 'FY_BY_CL1CKBUTTON'
# data['typoResult'] = 'true'
# data = {'i':content,
#         'from':'AUTO',
#         'to':'AUTO',
#         'smartresult':'dict',
#         'client':'fanyideskweb',
#         'doctype':'json',
#         'version':'2.1',
#         'keyfrom':'fanyi.web',
#         'typoResult':'true'}
#这个data不就是以字典的形式带入的吗，当我写成字典的格式来为什么我会报错呢？
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
print('翻译结果： %s' % (target['translateResult'][0][0]['tgt']))
if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
    loops(url)