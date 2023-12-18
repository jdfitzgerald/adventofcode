import pprint 
import re 
import os 
pp = pprint.PrettyPrinter(indent=2)

def poly_area(points):
    n = len(points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    area = abs(area) / 2.0
    return area

file = open(os.path.dirname(__file__)+'/real.data','r')
#file = open(os.path.dirname(__file__)+'/test.data','r')

last_point = (0,0)
points = [last_point]

total_dist = 0
max_i = 0
max_j = 0
for line in [l.strip() for l in file]:
    matches = re.search(r'([RDLU]) ([0-9]+) .#([0-9a-f]{6}).', line)

    dir = matches.group(1)
    dist = int(matches.group(2))
    colour = matches.group(3)

    dir = colour[-1]
    dist = int(colour[:-1],16)

    (i,j) = last_point

    max_i = max(max_i,i)
    max_j = max(max_j,j)
    match dir:
        case '0':
            point = (i,j+dist)
        case '1':
            point = (i+dist,j)
        case '2':
            point = (i,j-dist)
        case '3':
            point = (i-dist,j)
    points.append(point)
    last_point = point
    total_dist += dist



area = poly_area(points) + (total_dist//2) +1
pp.pprint(int(area))


"""
(i,j) = last_point

max_i = max(max_i,i)
max_j = max(max_j,j)
for i in range(max_i+1):
    for j in range(max_j+1):
        if (i,j) in points:
            print('#',end='')
        else:
            print('.',end='')
    print('')
    """