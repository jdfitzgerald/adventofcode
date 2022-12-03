import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
file = open('data','r')

def priority(c):
    n = ord(c)
    if n > 96: n -= 96
    else: n -= 38
    return n

pscore=0
for line in [l.strip() for l in file]:
    c1, c2 = line[:len(line)//2],line[len(line)//2:]
    item = set(c1).intersection(set(c2)).pop()
    pscore += priority(item)

print(pscore)
