#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import json

class vocab:
    def __init__(self):
        self.path="data/vocab.txt"
        self.vocab=set()

    def get_vocab(self, f):
        for ln in open(f,"r"):
            ln = ln.strip().decode("utf-8").split("\t")
            src = ln[0] + " " + ln[1]
            # print src
            words = src.split(" ")
            s = set(words)
            self.vocab = self.vocab | s
            # print self.vocab
        print len(self.vocab)


if __name__ == '__main__':
    vocab = vocab()
    vocab.get_vocab("data/data/demo.train")
    vocab.get_vocab("data/data/demo.dev")
    vocab.get_vocab("data/data/demo.test")
    vocab.get_vocab("data/demo.train")
    vocab.get_vocab("data/demo.test")
    vocab.get_vocab("data/demo.dev")
    f = open(vocab.path, "w")
    for word in vocab.vocab:
        print word
        f.write("%s\n" % word)

