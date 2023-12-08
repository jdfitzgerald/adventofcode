import pprint
pp = pprint.PrettyPrinter(indent=2)


#file = open('day05/real.data','r')
file = open('day05/test.data','r')

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
        r.append([dest_start, dest_start + l -1, src_start])
        line = file.readline().strip()

    mappings[src] = {'ranges':r, 'dest':dest}

    line = file.readline()
    if not line:
        break
    else:
        line = line.strip()

pp.pprint(mappings)

upper_bound=57075758
upper_bound=57075780
upper_bound=50

min_location = 9999999999999


for location in range(34,upper_bound):
    cur_value = location
    src = 'location'


    while src != 'seed':
        for r in mappings[src]['ranges']:
            if r[0] <= cur_value <= r[1]:
                cur_value = r[2] + (cur_value - r[0])
                break
        src = mappings[src]['dest']

    for s in seed_ranges:
        if s[0] <= cur_value <= s[1]:
            min_location = min(min_location, cur_value)
            break

    if location % 50000 == 0:
        print(location)

print(min_location)