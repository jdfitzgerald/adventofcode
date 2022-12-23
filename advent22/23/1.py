import pprint 
import os 
import numpy as np

pp = pprint.PrettyPrinter(indent=2)

#filename = os.path.dirname(__file__)+'/test'
filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')

elves = set()
for (y,line) in enumerate([l.strip() for l in file]):
    for x, c in enumerate(line):
        if c == '#':
            elves.add((x,y))

def check_move(elf,dir):
    (x,y) = dir
    checks = []
    if x == 0:
        checks.append(tuple(np.add(elf,(-1,y))))
        checks.append(tuple(np.add(elf,(0,y))))
        checks.append(tuple(np.add(elf,(1,y))))
    else:
        checks.append(tuple(np.add(elf,(x,-1))))
        checks.append(tuple(np.add(elf,(x,0))))
        checks.append(tuple(np.add(elf,(x,1))))
    
    for c in checks:
        if c in elves:
            return False
    return True

def check_adjacent(elf):
    checks = []
    checks.append(tuple(np.add(elf,(-1,1))))
    checks.append(tuple(np.add(elf,(0,1))))
    checks.append(tuple(np.add(elf,(1,1))))
    checks.append(tuple(np.add(elf,(-1,-1))))
    checks.append(tuple(np.add(elf,(0,-1))))
    checks.append(tuple(np.add(elf,(1,-1))))
    checks.append(tuple(np.add(elf,(1,0))))
    checks.append(tuple(np.add(elf,(-1,0))))
    for c in checks:
        if c in elves:
            return True
    return False


def gen_directions():
    while True:
        for m in [(0,-1),(0,1),(-1,0),(1,0)]:
            yield m

def elf_bounds():
    points = np.array(list(elves))
    min = np.min(points, 0)
    max = np.max(points, 0)
    return [min, max]

def print_elves():
    ((minx, miny), (maxx, maxy)) = elf_bounds()
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x,y) in elves:
                print('#',end='')
            else:
                print('.',end='')
        print('')
    print('')

direction = gen_directions()
for round in range(10):
    targets = {}
    directions = [next(direction) for i in range(4)]
    for elf in elves:
        if check_adjacent(elf):
            for dir in directions:
                if check_move(elf,dir):
                    move = tuple(np.add(elf,dir))
                    if move in targets:
                        targets[move] = False
                    else:
                        targets[move] = elf
                    break
    for new_elf in targets:
        old_elf = targets[new_elf]
        if old_elf:
            elves.add(new_elf)
            elves.remove(old_elf)
    
    next(direction)

((minx, miny), (maxx, maxy)) = elf_bounds()
area = (1+maxx-minx)*(1+maxy-miny)
space = area - len(elves)
print(space)
