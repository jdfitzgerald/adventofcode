import pprint
import math
pp = pprint.PrettyPrinter(indent=2)

file = open('day04/real.data','r')
#file = open('day04/test.data','r')
total = 0
for line in [l.strip() for l in file]:
    data = line.split(':')
    (winners,numbers) = [set(x.strip().split()) for x in data[1].strip().split('|')]
    score = math.floor(2 ** (len(winners&numbers)-1)) # floor fixes 0.5 for -1
    total += score

print(total)
