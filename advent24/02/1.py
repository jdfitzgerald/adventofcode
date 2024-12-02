import pprint
pp = pprint.PrettyPrinter(indent=2)


#file = open('day02/real.data','r')
#file = open('test.data','r')
file = open('real.data','r')

total = 0
for line in [l.strip() for l in file]:
    row = [int(x) for x in line.split()]
    last = row[0]
    last_d = last - row[1]
    safe = 1
    for x in row[1:]:
        d = last - x
        if not (1 <= abs(d) <= 3) or (d*last_d < 0):
            safe = 0
            break
        last_d = d
        last = x
    total = total + safe

print(total)
