import pprint 
import re

pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

num_stacks = len(file.readline())//4

stacks = [[] for i in range(0,num_stacks)]
pp.pprint(stacks)

p = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")

file.seek(0)
for line in file:
    if line.strip() == '' or line[1]=='1': continue

    if line[:4] != 'move':
        for i in range(0, num_stacks):
            pos = i*4 + 1
            if line[pos] != ' ': stacks[i].insert(0,line[pos])

    else: 
        [num, src, dest] = [int(x) for x in p.match(line).groups()]
        for i in range(num):
            stacks[dest-1].append(stacks[src-1].pop())


print("".join([s.pop() for s in stacks]))
