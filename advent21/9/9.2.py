import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

depths = []
for lnum, line in enumerate(file):
    depths.append([9 if int(x)==9 else 1 for x in line.strip()])

max_y = len(depths) - 1
max_x = len(depths[0]) - 1

def mark_basin(x, y):
    if depths[y][x] == 0 or depths[y][x] == 9:
        return 0

    size = 1
    depths[y][x] = 0
    if x > 0: size += mark_basin(x-1, y)
    if y > 0: size += mark_basin(x, y-1)
    if x < max_x: size += mark_basin(x+1, y)
    if y < max_y: size += mark_basin(x, y+1)
    
    return size

sizes = []
for y in range(0, max_y+1):
    for x in range(0, max_x+1):
        if depths[y][x] == 1:
            sizes.append(mark_basin(x,y))

import functools
pp.pprint(functools.reduce(lambda a,b: a*b, sorted(sizes)[-3:]))
