import pprint 
import os 
from collections import deque

pp = pprint.PrettyPrinter(indent=2)


grid = []
file = open(os.path.dirname(__file__)+'/real.data','r')
#file = open(os.path.dirname(__file__)+'/test.data','r')
for line in [l.strip() for l in file]:
    grid.append(line)

height = len(grid)
width = len(grid[0])

def shoot_beam(i,j,vi,vj):
    # beam is a position and a direction (0,1 => east, etc)
    beams = deque([(i,j,vi,vj)])

    activated = set()
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
    return len(points)


max_active = 0
for i in range(height):
    activated = shoot_beam(i,0,0,1)
    max_active = max(max_active,activated)
    activated = shoot_beam(i,width-1,0,-1)
    max_active = max(max_active,activated)

for j in range(width):
    activated = shoot_beam(0,j,1,0)
    max_active = max(max_active,activated)
    activated = shoot_beam(0,height-1,-1,0)
    max_active = max(max_active,activated)

print(max_active)