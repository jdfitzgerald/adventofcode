import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
#file = open('data','r')



rules = {}
for n,line in enumerate(file):
    if n == 0: start = line.strip()
    if n > 1: rules.update([line.strip().split(' -> ')])


import functools 
@functools.lru_cache(maxsize=None)
def expand_pair(pair, steps):
    if steps == 0: return pair
    nc = rules[pair]
    return expand_pair(pair[0]+nc, steps-1)[0:-1]+expand_pair(nc+pair[1],steps-1)
    



result = ''
steps = 22
for c in range(1, len(start)):
    pair=start[c-1:c+1]
    result += expand_pair(pair, steps)



from collections import Counter
counts=Counter(result)

print(max(counts.values()) - min(counts.values()))
