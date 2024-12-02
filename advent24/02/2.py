import pprint
pp = pprint.PrettyPrinter(indent=2)

# 484 is wrong

#file = open('02/test.data','r')
file = open('02/real.data','r')

def check_list(row, skips):
    safe = 1

    for i,x in enumerate(row):
        if i == 0:
            last = row[0]
            last_d = last - row[1]
            continue

        d = last - x
        if not (1 <= abs(d) <= 3) or (d*last_d < 0):
            if skips == 0:
                skips = 1
                safe = check_list(row[:i]+row[(i+1):],skips)
                if safe: break

                safe = check_list(row[:(i-1)]+row[i:],skips)
                if safe: break

                safe = check_list(row[:(i-2)]+row[i-1:],skips)

                break
            safe = 0
            break
        last_d = d
        last = x
    print(row,safe)
    return safe


total = 0
for line in [l.strip() for l in file]:
    row = [int(x) for x in line.split()]

    print('x',row)

    safe = check_list(row,0)

    if safe == 0:
        print(row, safe)
    total = total + safe

print(total)
