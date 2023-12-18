import pprint 
import os 
import copy 
from collections import deque
pp = pprint.PrettyPrinter(indent=2)


#file = open(os.path.dirname(__file__)+'/real.data','r')
file = open(os.path.dirname(__file__)+'/test.data','r')

grid = []

for line in [l.strip() for l in file]:
    grid.append([int(x) for x in line])

grid[0][0]=0
pp.pprint(grid)

height = len(grid)
width = len(grid[0])
dest = (height-1, width-1)


def get_next(pos,d):
    (i,j) = pos
    match d:
        case 'N':
            i -= 1
        case 'S':
            i += 1
        case 'E':
            j += 1
        case 'W':
            j -= 1
    if 0 <= i < height and 0 <= j < width:
        return (i,j)
    else:
        return None

right_lefts = {
    'N' : ('E','W'),
    'S' : ('W','E'),
    'E' : ('S','N'),
    'W' : ('N','S'),
}

init = [{
    'pos':(0,0),
    'heat_loss':0,
    'dir':'E',
    'straight':0
}]
stack=deque(init)

min_cost = 99999999999999

# visited is flawed - visits can happen with diff routes - so needs to be tracked per point or done differently
visited = set()
while stack:
    current = stack.pop()
    pos = current['pos']
    dir = current['dir']
    heat_loss = grid[pos[0]][pos[1]] + current['heat_loss']

    if pos == dest:
        min_cost = min(min_cost, heat_loss)
        continue

    if pos in visited:
        continue
    visited.add(pos)

    print(pos, dir, heat_loss, current['straight'])

    if heat_loss > min_cost:
        continue

    (right,left) = right_lefts[dir]

    #right
    rpos = get_next(pos,right)
    if rpos is not None:
        next = {
            'pos': rpos,
            'heat_loss': heat_loss,
            'straight': 1,
            'dir': right
        }
        stack.append(next)
    #left
    lpos = get_next(pos,left)
    if lpos is not None:
        next = {
            'pos': lpos,
            'heat_loss': heat_loss,
            'straight': 1,
            'dir': left
        }
        stack.append(next)


    if current['straight'] < 3:
        spos = get_next(pos,dir)
        if spos is not None:
            next = {
                'pos': spos,
                'heat_loss': heat_loss,
                'straight': current['straight'] + 1,
                'dir': dir
            }
            stack.append(next)

