import pprint
pp = pprint.PrettyPrinter(indent=2)


#file = open('day05/real.data','r')
file = open('day05/test.data','r')

# total seeds 2,217,452,483
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
        r.append([src_start, src_start + l -1, dest_start, dest_start + l -1])
        line = file.readline().strip()

    mappings[src] = {'ranges':r, 'dest':dest}

    line = file.readline()
    if not line:
        break
    else:
        line = line.strip()

pp.pprint(mappings)
# parsing above is ugly and inefficient


current = 'seed'
while True:
    for range in mappings[current]['ranges']:
        up_next = mappings[current]['dest']
        print('-----')
        print(range)
        print(up_next)
        #x.in 23-40 13-30
        #x.out 10-27 28-41
        #y.in 12-28 30-31 1-2
        #y.out 2-18 29-30 31-40
        # collapsed.in:  1-2  23-24 25-40 13 14 15-16 17-30
        # collapsed.out:31-40 10-11 2-17  18 29 29-30 32-41

        for rx in mappings[up_next]['ranges']:
            if range[2] <= rx[1] and rx[0] <= range[3]:
                print('overlap',range,rx)

    break

exit()



min_location = 99999999
seeds_checked = 0
for i in range(0,len(seeds),2):
    print(i,' of ', len(seeds)/2)
    print(seeds[i],' to ', seeds[i] + seeds[i+1])
    for seed in range(seeds[i], seeds[i]+seeds[i+1]):
        cur_value = seed
        src = 'seed'

        while src != 'location':
            for r in mappings[src]['ranges']:
                if r[0] <= cur_value <= r[1]:
                    cur_value = r[2] + (cur_value - r[0])
                    break

            src = mappings[src]['dest']
        min_location = min(min_location, cur_value)
        seeds_checked += 1
        if seeds_checked % 50000 == 0:
            print(seeds_checked)

print(min_location)
