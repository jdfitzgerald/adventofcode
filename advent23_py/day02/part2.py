import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day02/real.data','r')
#file = open('day02/test.data','r')

total = 0
for line in [l.strip() for l in file]:
    bag = {'red':0,'green':0,'blue':0}
    (game, handfuls) = [x.strip() for x in line.split(":")]
    game_id = int(game.split(' ')[1])

    for handful in handfuls.split(';'):
        for (n, colour) in [c.strip().split(' ') for c in handful.split(',')]:
            bag[colour] = max(bag[colour], int(n))
    
    total = total + (bag['red'] * bag['blue'] * bag['green'])
print(total)