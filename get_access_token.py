# coding=utf-8

import urllib, urllib2, sys
import ssl
import json

def get_access_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6uG8MRKKnzMsro1Ag3QjvWXT&client_secret=sz99x8xMzSm3UBipUvmij2ESOBz8QILa'
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        # print(content)
        content=json.loads(content)
        # print content["access_token"]
    return content["access_token"]

if __name__ == '__main__':
    get_access_token()