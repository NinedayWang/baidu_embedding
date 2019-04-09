# coding:utf-8
import urllib, urllib2, sys
import ssl
import json
from get_access_token import get_access_token

access_token=get_access_token()
url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/wordembedding?' \
      'access_token='+access_token
post_data = {"query1":"百度","query2":"谷歌","tid":1}
encodedata=json.dumps(post_data).encode('GBK')
request = urllib2.Request(url, encodedata)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)