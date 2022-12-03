import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

def priority(c):
    n = ord(c)
    if n > 96: n -= 96
    else: n -= 38
    return n

pscore=0
group = []
index = 0
for line in [l.strip() for l in file]:
    group += [set(line)]
    index += 1
    if index % 3 == 0: 
        index = 0
        badge = group[0].intersection(group[1].intersection(group[2])).pop()
        group = []
        pscore += priority(badge)

print(pscore)
