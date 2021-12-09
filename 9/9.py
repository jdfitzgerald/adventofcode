import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
file = open('data','r')

depths = []
for lnum, line in enumerate(file):
    depths.append([int(x) for x in line.strip()])

max_y = len(depths) - 1
max_x = len(depths[0]) - 1

lows = []
for y,row in enumerate(depths):
    for x,d in enumerate(row):
        if x > 0 and d>=depths[y][x-1]: continue
        if y > 0 and d>=depths[y-1][x]: continue
        if x < max_x and d>=depths[y][x+1]: continue
        if y < max_y and d>=depths[y+1][x]: continue
        lows.append(d+1)


print(sum(lows))


