import pprint 
import re
import sys

pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

grid={}

rex = r"x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)"
target_row = 10
max_x, min_x = -sys.maxsize, sys.maxsize

for line in [l.strip() for l in file]:
    (sx,sy,bx,by) = [int(x) for x in re.search(rex, line).groups()]
    
    radius = 1+ abs(sx-bx) + abs(sy-by)
    max_x = max(sx+radius, max_x)
    min_x = min(sx-radius, min_x)
    for y in range(0,radius):
        if sy+y not in grid.keys():
            grid[sy+y] = {}
        if sy-y not in grid.keys():
            grid[sy-y] = {}
        for x in range(0,radius-y):
            grid[sy+y][sx+x] = '#'
            grid[sy-y][sx+x] = '#'
            grid[sy+y][sx-x] = '#'
            grid[sy-y][sx-x] = '#'

    grid[sy][sx] = 'S'
    grid[by][bx] = 'B'

ys = list(grid.keys())
ys.sort()
for y in ys:
    for x in range(min_x,max_x):
        if x in grid[y]:
            print(grid[y][x], end='')
        else:
            print('.', end='')
    print(y)

print(len([1 for g in grid[target_row] if g != 'B']))

