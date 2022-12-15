import pprint 
import re

pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

grid={}

rex = r"x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)"

pmin,pmax = 0,4000001

ranges={}
for y in range(pmin,pmax):
    ranges[y] = []

for line in [l.strip() for l in file]:
    print(line)
    (sx,sy,bx,by) = [int(x) for x in re.search(rex, line).groups()]
    radius = abs(sx-bx) + abs(sy-by)
    ymin = max(sy-radius,pmin)
    ymax = min(sy+radius,pmax)

    for y in range(ymin,ymax):
        width = radius - abs(sy-y)
        ranges[y].append((sx-width, sx+width))


for y in ranges.keys():
    if y%10000==0: print(y)
    combined = []
    ranges[y].sort()
    last = ranges[y][0]
    combined.append(last)
    for i in range(1,len(ranges[y])):
        cur = ranges[y][i]
        last = combined[len(combined)-1]
        if cur[0] <= last[1]+1 and cur[1] > last[1]:
            combined.pop()
            combined.append((last[0], cur[1]))
        elif cur[0] > last[1]+1:
            combined.append(cur)
    ranges[y] = combined
for y,r in [(x,ranges[x]) for x in ranges if len(ranges[x])>1]:
    print(y)
    print(r[0][1], r[1][0])
    print(y+(4000000*((r[1][0] + r[0][1])//2)))
