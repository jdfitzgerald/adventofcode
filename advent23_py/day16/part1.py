import pprint 
import os 
from collections import deque

pp = pprint.PrettyPrinter(indent=2)


grid = []
file = open(os.path.dirname(__file__)+'/real.data','r')
#file = open(os.path.dirname(__file__)+'/test.data','r')
for line in [l.strip() for l in file]:
    pp.pprint(line)
    grid.append(line)

activated = set()
# beam is a position and a direction (0,1 => east, etc)
beams = deque([(0,0,0,1)])

height = len(grid)
width = len(grid[0])

while len(beams):
    # take each beam and do one step
    (i,j,vi,vj) = beams.pop()

    if (i,j,vi,vj) in activated: # loop avoidance
        continue

    if i >= height or j >= width or i<0 or j<0:
        continue
    activated.add((i,j,vi,vj))
    action = grid[i][j]

    match action:
        case '\\':
            beams.appendleft((i+vj, j+vi, vj, vi))
        case '/':
            beams.appendleft((i-vj, j-vi, -vj, -vi))
        case '-':
            if vi == 0:
                beams.appendleft((i, j+vj, vi, vj))
            else:
                beams.appendleft((i, j-1, 0, -1))
                beams.appendleft((i, j+1, 0, 1))
        case '|':
            if vj == 0:
                beams.appendleft((i+vi, j, vi, vj))
            else:
                beams.appendleft((i-1, j, -1, 0))
                beams.appendleft((i+1, j, 1, 0))
        case '.':
                beams.appendleft((i+vi, j+vj, vi, vj))

points = {(i,j) for (i,j,_,_) in activated}
print(len(points))