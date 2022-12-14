import pprint 
import numpy as np

pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')


def drop_sand(x,y):
    if y > max_y: return y
    elif (x,y+1) not in rocks: return drop_sand(x,y+1)
    elif (x-1,y+1) not in rocks: return drop_sand(x-1,y+1)
    elif (x+1,y+1) not in rocks: return drop_sand(x+1,y+1)
    else: 
        rocks.add((x,y))
        return y


rocks = set()

for line in [l.strip() for l in file]:
    last_pos = None
    for cur_pos in [eval('('+c+')') for c in line.split(' -> ')]:
        rocks.add(cur_pos)
        if last_pos is not None:
            (steps_i,steps_j) = np.subtract(cur_pos,last_pos)
            if steps_i != 0:
                for i in range(last_pos[0], steps_i+last_pos[0], steps_i//abs(steps_i)):
                    rocks.add((i, last_pos[1]))
            else:
                for j in range(last_pos[1], steps_j+last_pos[1], steps_j//abs(steps_j)):
                    rocks.add((last_pos[0],j))
        last_pos = cur_pos

max_y = max([p[1] for p in rocks])


count = 0
while drop_sand(500,-1) <= max_y:
    count += 1
    if count > 1000: break

print(count)

