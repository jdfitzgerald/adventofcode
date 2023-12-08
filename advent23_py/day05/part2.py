import pprint
import time
import functools
pp = pprint.PrettyPrinter(indent=2)


file = open('day05/real.data','r')
#file = open('day05/test.data','r')

seeds = [int(x) for x in file.readline().strip().split()[1::]]
seed_ranges = []

for i in range(0,len(seeds),2):
    seed_ranges.append([seeds[i], seeds[i]+seeds[i+1]])

pp.pprint(seed_ranges)

mappings = {}

line = file.readline()
line = file.readline().strip()
while True:
    # reversing source and dest to go backwards
    (dest,_,src) = line.split(' ')[0].split('-')

    r = []
    line = file.readline().strip()
    while line:
        (dest_start, src_start, l) = [int(x) for x in line.split()]
        r.append((dest_start, dest_start + l -1, src_start-dest_start))
        line = file.readline().strip()
    
    r.sort()
    r = tuple(r)

    mappings[src] = {'ranges':r, 'dest':dest}

    line = file.readline()
    if not line:
        break
    else:
        line = line.strip()

pp.pprint(mappings)

upper_bound=57075758 +1 # result from pt 1

min_location = -1
 
# binary search ends up ~40% faster - 1500ms vs 2500ms per 50000
# memoization made this slower
# realised that debug mode was actually the real timesink
def map_value(src, v, ranges):
    low = 0
    high = len(ranges) -1
    while low <= high:
        mid = (low + high) //2
        if  v < ranges[mid][0]:
            high = mid -1
        elif ranges[mid][0] <= v <= ranges[mid][1]:
            return v + ranges[mid][2]
        else:
            low = mid +1
    return v


checkpt = round(time.time() * 1000)

for location in range(0,upper_bound):
    cur_value = location
    src = 'location'

    while src != 'seed':
        cur_value = map_value(src,cur_value, mappings[src]['ranges'])
        src = mappings[src]['dest']

    for s in seed_ranges:
        if s[0] <= cur_value <= s[1]:
            min_location = location
            break

    if min_location > -1:
        break

    if location % 50000 == 0:
        now = round(time.time() * 1000)
        
        print(now - checkpt)
        checkpt = now
        print(location)

print(min_location)