# -*- coding:utf-8 -*-

import re
import string
from collections import Counter    


class SpellingCorrector():
    
    def __init__(self, filepath="big.txt"):
        with open(filepath, "r") as filer:
            words = Counter(self.tokenize(filer.read()))
            #words = Counter(re.findall(r"\w+", filer.read().lower()))
        N = sum(words.values())
        self.word2prob = dict([(word, words[word]*1.0/N) for word in words])
        
    def tokenize(self, text):
        return re.findall("[a-z]+", text.lower())
        
    def load_dictionary(self, filepath="big.txt"):
        with open(filepath, "r") as filer:
            words = Counter(re.findall(r"\w+", filer.read().lower()))
        N = sum(words.values())
        self.word2prob = dict([(word, words[word]*1.0/N) for word in words])
    
    def one_edit_candidate(self, word):
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in string.ascii_lowercase]
        inserts = [L + c + R for L, R in splits for c in string.ascii_lowercase]
        return set(deletes + transposes + replaces + inserts)
    
    def two_edit_candidate(self, word):
        return (e2 for e1 in self.one_edit_candidate(word) for e2 in self.one_edit_candidate(e1))
    
    def correct(self, word):
        if word in self.word2prob:
            return word
        else:
            one_edits = set(w for w in self.one_edit_candidate(word) if w in self.word2prob)
            two_edits = set(w for w in self.two_edit_candidate(word) if w in self.word2prob)
            candidates = one_edits | two_edits
            return max(candidates, key=lambda word: self.word2prob[word])
        
    def suggest(self, word, top_k):
        one_edits = set(w for w in self.one_edit_candidate(word) if w in self.word2prob)
        two_edits = set(w for w in self.two_edit_candidate(word) if w in self.word2prob)
        candidates = one_edits | two_edits
        if word in self.word2prob:
            candidates |= set([word])
        return sorted(candidates, key=lambda word: self.word2prob[word])[:top_k]
    
if __name__ == "__main__":
    corrector = SpellingCorrector()
    print(corrector.correct("speling"))
    print(corrector.suggest("speling", top_k=5))
    print(corrector.correct("korrectud"))
    print(corrector.suggest("korrectud", top_k=5))
    print(corrector.correct("spelling"))
    print(corrector.suggest("spelling", top_k=5))
    print()
    pass
        
        