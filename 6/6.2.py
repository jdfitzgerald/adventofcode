import pprint 
pp = pprint.PrettyPrinter(indent=2)

import functools 


#file = open('test','r')
file = open('data','r')

l = file.readline()
fish = [int(t) for t in l.split(',')]

cycle = 7
days = 256

@functools.lru_cache(maxsize=None)
def spawn_fish(f,days):
    if days < cycle: return 1

    first_born = days-f;
    kids = sum([spawn_fish(8, d-1) for d in range(first_born, 0, -cycle)])
    return kids +1
    

total = sum([spawn_fish(f,days) for f in fish])
print(total)


