# -*- coding:utf-8 -*-

import re
import string
from collections import Counter, namedtuple

class Candidater():
    
    def __init__(self, vocab, order):
        self.vocab = vocab
        self.order = order
    
    def step(self, word):
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in self.vocab]
        inserts = [L + c + R for L, R in splits for c in self.vocab]
        return inserts, deletes, replaces, transposes
    
    def __call__(self, word):
        rcandidate = {}
        for i in self.order:
            rcandidate[i] = {}
            inserts, deletes, replaces, transposes = self.step(word) if i == 0 else rcandidate[i][""]
            rcandidate[i]["inserts"] = inserts
            rcandidate[i]["deletes"] = deletes
            rcandidate[i]["replaces"] = replaces
            rcandidate[i]["transposes"] = transposes