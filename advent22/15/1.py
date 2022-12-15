import pprint 
import re

pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
target_row = 10
file = open('data','r')
target_row = 2000000

grid={}

rex = r"x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)"

ranges=[]
for line in [l.strip() for l in file]:
    (sx,sy,bx,by) = [int(x) for x in re.search(rex, line).groups()]
    radius = abs(sx-bx) + abs(sy-by)
    
    if sy-radius <= target_row and target_row <= sy+radius:
       width = radius - abs(sy-target_row) 
       ranges.append((sx-width,sx+width))

combined = []
ranges.sort()
last = ranges[0]
combined.append(last)
for i in range(1,len(ranges)):
    last = combined.pop()
    if ranges[i][0] < last[1]:
        combined.append((last[0], ranges[i][1]))
    else:
        combined.append(last)
        combined.append(ranges[i])

pp.pprint(combined)
start = combined[0][0]
end = combined.pop()[1]
print(end-start)