import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')



rules = {}
for n,line in enumerate(file):
    if n == 0: start = line.strip()
    if n > 1: rules.update([line.strip().split(' -> ')])

import string
alphabet = dict.fromkeys(string.ascii_uppercase, 0)

import functools 
@functools.lru_cache(maxsize=None)
def expand_pair(pair, steps):
    if steps == 0: 
        counts = alphabet.copy()
        counts[pair[1]]=1
        return counts

    nc = rules[pair]
    left = expand_pair(pair[0]+nc, steps-1)
    right = expand_pair(nc+pair[1],steps-1)
    return {k: left.get(k, 0) + right.get(k, 0) for k in set(right) | set(left)}
    

results = {}
steps = 40
for c in range(1, len(start)):
    pair=start[c-1:c+1]
    this_pair = expand_pair(pair, steps)
    results = {k: this_pair.get(k, 0) + results.get(k, 0) for k in set(results) | set(this_pair)}

results = ({k:results.get(k) for k in results if results.get(k) > 0})

print(max(results.values()) - min(results.values()))
