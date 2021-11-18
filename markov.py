from collections import defaultdict
from random import randint
import sys

END = '\x90'

#ngrams -> list of next word
ngrams = defaultdict(list)

def build(filename):
    """build the ngram->wordlist map"""

    #read in all words
    with open(filename) as f:
        words = [w for line in f for w in line.split()]

    #padd it out - probably a more clever way...
    while len(words)%3 != 0:
        words.append(END)

    #build 2gram -> words
    for i in range(len(words)-2):
        w0 = words[i].strip()
        w1 = words[i+1].strip()
        w2 = words[i+2].strip()
        ngrams[(w0,w1)].append(w2)

def randngram():
    """get a random ngram"""
    
    keys = list(ngrams.keys()) #fixme
    return keys[randint(0,len(keys)-1)]

def randword(words):
    """get a random word from a list of words"""
    
    if not words: return END
    return words[randint(0,len(words)-1)] if len(words) > 0 else words[0]

def gen(nwords=1000):
    """generate nwords using the ngrams map"""

    k = randngram()
    print(f'{k[0]} {k[1]}', end=' ')
    c = 2
    while c < nwords:
        cands = ngrams[k]
        w = randword(cands)
        if w == END: 
            k = randngram()
            continue
        print(w, end=' ')
        k = (k[1], w)
        c += 1
    print()

if __name__ == '__main__':
    build(sys.argv[1])
    gen()
