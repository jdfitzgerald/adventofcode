import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

steps = { 'noop': 1, 'addx':2 }

cycle = 0
X = 1
for line in [l.strip().split(' ') for l in file]:
    cmd = line[0]
    for i in range(steps[cmd]):
        if cycle % 40 == 0: print('')
        print(('#' if cycle % 40 in [X-1,X,X+1] else '.'), end='')
        cycle += 1

    if cmd == 'addx': X += int(line[1])

