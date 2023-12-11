import re
import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day11/real.data','r')
#file = open('day11/test.data','r')
galaxies = []


for (i,line) in enumerate([l.strip() for l in file]):
    galaxies += [[i,m.start()] for m in re.finditer('#', line)]

height = i+1
width = len(line)

# could split out the two with zip *galaxies, but this feels clearer
expanding_rows = {i for (i,j) in galaxies}.symmetric_difference(range(0,height))
expanding_cols = {j for (i,j) in galaxies}.symmetric_difference(range(0,width))

for g in galaxies:
    g[0] += sum([ 1 for i in expanding_rows if i < g[0]])
    g[1] += sum([ 1 for i in expanding_cols if i < g[1]])

num_galaxies = len(galaxies)

total_dist = 0
for s in range(0, num_galaxies):
    src = galaxies[s]
    for d in range(s, num_galaxies):
        dest = galaxies[d]
        dist = abs(src[0]-dest[0]) + abs(src[1]-dest[1])
        print(src, dest, dist)
        total_dist += dist

print(total_dist)