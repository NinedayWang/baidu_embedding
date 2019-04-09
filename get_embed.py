#!/bin/env python
#coding:utf-8
#

'''
'''

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import time
import chardet
import requests
import json
from get_access_token import get_access_token


class embed:
    def __init__(self):
        self.access_token=get_access_token()
        self.url = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_vec' \
                   '?access_token='+self.access_token

    def embed(self, word):

        headers = {
            'Content-Type' : 'application/json'
        }

        body = {
            "word":word,
            "dem":300
        }

        encodedata = json.dumps(body).encode('GBK')

        r = requests.post(self.url, data=encodedata, headers=headers)
        # print r.text
        result = json.loads(r.text)
        if "word" in result.keys():
            # print result["word"]
            print word + " " + " ".join(map(str,result["vec"]))
            return word + " " + " ".join(map(str,result["vec"]))

if __name__ == '__main__':
    embed = embed()
    f = open("data/vocab.txt","r")
    emb_f = open("data/emb.txt","a")
    for ln in f:
        try:
            emb = embed.embed(ln.strip())
        except:
            print "Max retries"
            time.sleep(1)
            emb = embed.embed(ln.strip())
            if emb is not None:
                emb_f.write("%s\n" % emb)
        else:
            if emb is not None:
                emb_f.write("%s\n" % emb)


