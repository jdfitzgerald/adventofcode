import pprint 
import numpy as np
pp = pprint.PrettyPrinter(indent=2)

#file = open('test2','r')
file = open('data','r')

directions = {
        'R': (1,0),
        'L': (-1,0),
        'U': (0,1),
        'D': (0,-1)
        }

rope = [(0,0) for i in range(0,10)]
visited = set()
visited.add(rope[9])
for (d,steps) in [l.strip().split(' ') for l in file]:
    delta = directions[d]
    for i in range(int(steps)):
        rope[0] = np.add(rope[0],delta)
        for k in range(1,len(rope)):
            dist = np.subtract(rope[k-1],rope[k])
            if (abs(dist[0]) == 2) or (abs(dist[1]) == 2):
                tail_delta = [p//abs(p) if p!=0 else 0 for p in dist]
                rope[k] = tuple(np.add(rope[k], tail_delta))
        visited.add(rope[9])

print(len(visited))
