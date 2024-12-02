import pprint
pp = pprint.PrettyPrinter(indent=2)


#file = open('day02/real.data','r')
file = open('02/test.data','r')
#file = open('02/real.data','r')

def check_list(last, last_d, row, skips):
    safe = 1
    for i,x in row[1:]:
        d = last - x
        if not (1 <= abs(d) <= 3) or (d*last_d < 0):
            if skips == 0:
                skips = 1
                if i = len(row)-1: #special case for last
                    break
                # skip this
                check_list(last,last_d,row[i+1:],skips)

                # skip next
                check_list(last,last_d,row[i+1:],skips)

                continue
            safe = 0
            break
        last_d = d
        last = x
    return (safe,skips)


total = 0
for line in [l.strip() for l in file]:
    row = [int(x) for x in line.split()]
    last = row[0]
    last_d = last - row[1]
    skips = 0

    (safe,skips) = check_list(last, last_d, row, skips)

    if safe == 0:
        print(row, safe, skips)
    total = total + safe

print(total)
