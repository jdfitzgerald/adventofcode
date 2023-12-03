import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day03/real.data','r')
#file = open('day03/test.data','r')

symbols = {}
numbers = []

new_number = ''

for (y,line) in enumerate([l.strip() for l in file]):
    symbols[y] = {}
    for (x,c) in enumerate(line):
        if c.isdigit():
            new_number += c
            continue
        elif c != '.':
            symbols[y][x] = c
        
        if new_number != '':
            numbers.append({'num':int(new_number), 'y':y, 'start_x':x-(len(new_number)), 'end_x': x-1})
            new_number = ''
        
    if new_number != '':
        numbers.append({'num':int(new_number), 'y':y, 'start_x':x-(len(new_number)), 'end_x': x-1})
        

pp.pprint(symbols)
pp.pprint(numbers)

sum_part_nos = 0

for n in numbers:
    is_part_number = False;
    min_y = max(0,n['y']-1)
    max_y = min(len(symbols)-1,n['y']+1)
    for y in range(min_y,max_y+1):
        for x in symbols[y]:
            if n['start_x']-1 <= x <= n['end_x'] +1:
                is_part_number = True
                break
        if is_part_number:
            sum_part_nos += n['num']
            break


print(sum_part_nos)