import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

steps = { 'noop': 1, 'addx':2 }

score = 0
cycle = 0
X = 1
for line in [l.strip().split(' ') for l in file]:
    cmd = line[0]
    for i in range(steps[cmd]):
        cycle += 1
        if (cycle-20) % 40 == 0:
            score += cycle*X

    if cmd == 'addx': X += int(line[1])

print(score)
