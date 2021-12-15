import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')


rules = {}
for n,line in enumerate(file):
    if n == 0: polymer = line.strip()
    if n > 1: rules.update([line.strip().split(' -> ')])

for i in range(0,10):
    next_polymer = ''
    for c in range(1, len(polymer)):
        pair=polymer[c-1:c+1]
        next_polymer += pair[0] + rules[pair]

    polymer = next_polymer + pair[1]


from collections import Counter
counts=Counter(polymer)

print(max(counts.values()) - min(counts.values()))
