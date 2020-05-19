from collections import Counter

###########################################################

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        key = str(args) + str(kwargs)
        helper.c[key] += 1
        return func(*args, **kwargs)
    helper.c = Counter()
    helper.calls = 0
    return helper

def memoize(func):
    mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]
    return memoizer

###########################################################

@call_counter
def LD(s, t):
    if s == "": return len(t)
    if t == "": return len(s)
    cost = 0 if s[-1] == t[-1] else 1
    res = min(
        [
            LD(s[:-1], t) + 1, 
            LD(s, t[:-1]) + 1, 
            LD(s[:-1], t[:-1]) + cost
        ]
    )
    return res

###########################################################

memo = {}
@call_counter
def levenshtein(s, t):
    if s == "": return len(t)
    if t == "": return len(s)
    cost = 0 if s[-1] == t[-1] else 1
    i1 = (s[:-1], t)
    if not i1 in memo:
        memo[i1] = levenshtein(*i1)
    i2 = (s, t[:-1])
    if not i2 in memo:
        memo[i2] = levenshtein(*i2)
    i3 = (s[:-1], t[:-1])
    if not i3 in memo:
        memo[i3] = levenshtein(*i3)
    res = min([memo[i1] + 1, memo[i2] + 1, memo[i3] + cost])
    return res

###########################################################

@call_counter
@memoize
def levenshteinA(s, t):
    if s == "": return len(t)
    if t == "": return len(s)
    cost = 0 if s[-1] == t[-1] else 1
    res = min([levenshteinA(s[:-1], t) + 1, levenshteinA(s, t[:-1]) + 1, levenshteinA(s[:-1], t[:-1]) + cost])
    return res

###########################################################



###########################################################

print(LD("Python", "Peithen"))
print("LD was called " + str(LD.calls) + " times!")

###########################################################

print(levenshtein("Python", "Pethno"))
print("The function was called " + str(levenshtein.calls) + " times!")

###########################################################

print(levenshteinA("Python", "Pethno"))
print("The function was called " + str(levenshteinA.calls) + " times!")