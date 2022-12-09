import pprint 
import numpy as np
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

directions = {
        'R': (1,0),
        'L': (-1,0),
        'U': (0,1),
        'D': (0,-1)
        }

head = [0,0]
tail = (0,0)
visited = set()
visited.add(tail)
for (d,steps) in [l.strip().split(' ') for l in file]:
    delta = directions[d]
    for i in range(int(steps)):
        head = np.add(head,delta)
        dist = np.subtract(head,tail)
        if (abs(dist[0]) == 2) or (abs(dist[1]) == 2):
            tail_delta = [p//abs(p) if p!=0 else 0 for p in dist]
            tail = tuple(np.add(tail, tail_delta))
            visited.add(tail)

print(len(visited))
