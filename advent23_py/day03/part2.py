import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day03/real.data','r')
#file = open('day03/test.data','r')

gears = {}
numbers = {}

new_number = ''

for (y,line) in enumerate([l.strip() for l in file]):
    gears[y] = {}
    numbers[y] = []
    for (x,c) in enumerate(line):
        if c.isdigit():
            new_number += c
            continue
        elif c == '*':
            gears[y][x] = c
        
        if new_number != '':
            numbers[y].append({'num':int(new_number), 'y':y, 'start_x':x-(len(new_number)), 'end_x': x-1})
            new_number = ''
        
    if new_number != '':
        numbers[y].append({'num':int(new_number), 'y':y, 'start_x':x-(len(new_number)), 'end_x': x-1})
        
num_rows = y


total = 0
for (y,x) in [(y,x) for y in gears for x in gears[y]]:
    nums = []
    low_y = max(0,y-1)
    high_y = min(num_rows,y+1)
    for yi in range(low_y,high_y+1):
        nums += [n['num'] for n in numbers[yi] if n['start_x']-1 <= x <= n['end_x'] +1]
    if len(nums) == 2:
        total += nums[0] * nums[1]

print(total)

