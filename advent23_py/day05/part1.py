import pprint
pp = pprint.PrettyPrinter(indent=2)


file = open('day05/real.data','r')
#file = open('day05/test.data','r')

seeds = [int(x) for x in file.readline().strip().split()[1::]]
pp.pprint(seeds)

mappings = {}

line = file.readline()
line = file.readline().strip()
while True:
    (src,_,dest) = line.split(' ')[0].split('-')

    r = []
    line = file.readline().strip()
    while line:
        (dest_start, src_start, l) = [int(x) for x in line.split()]
        r.append([src_start, src_start + l -1, dest_start])
        line = file.readline().strip()

    mappings[src] = {'ranges':r, 'dest':dest}

    line = file.readline()
    if not line:
        break
    else:
        line = line.strip()

pp.pprint(mappings)
# parsing above is ugly and inefficient

min_location = 99999999
for seed in seeds:
    cur_value = seed
    src = 'seed'


    while src != 'location':
        for r in mappings[src]['ranges']:
            if r[0] <= cur_value <= r[1]:
                cur_value = r[2] + (cur_value - r[0])
                break

        src = mappings[src]['dest']
    min_location = min(min_location, cur_value)

print(min_location)
