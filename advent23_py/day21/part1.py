import pprint 
import os 
import copy
pp = pprint.PrettyPrinter(indent=2)


file = open(os.path.dirname(__file__)+'/real.data','r')
#file = open(os.path.dirname(__file__)+'/test.data','r')

grid = []
for line in [l.strip() for l in file]:
    if 'S' in line:
        startpos = (len(grid), line.find('S'))
        line = line.replace('S','.')

    grid.append(list(line))


pp.pprint(startpos)
pp.pprint(grid)

def test_loc(y,x):
    if 0 <= y < len(grid) and 0 <= x <= len(grid[0]):
        if grid[y][x] == '.':
            return True
    return False

steps = 64 # result shuold be 16
next_locs = set()
next_locs.add(startpos)
for s in range(steps):
    cur_locs = copy.copy(next_locs)
    next_locs = set()
    while cur_locs:
        (y,x) = cur_locs.pop()
        if test_loc(y+1, x):
            next_locs.add((y+1, x))
        if test_loc(y-1, x):
            next_locs.add((y-1, x))
        if test_loc(y, x+1):
            next_locs.add((y, x+1))
        if test_loc(y, x-1):
            next_locs.add((y, x-1))
    print('----',s+1, len(next_locs))

