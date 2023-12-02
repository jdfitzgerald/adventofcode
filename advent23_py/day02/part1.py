import pprint 
pp = pprint.PrettyPrinter(indent=2)


#file = open('day02/real.data','r')
file = open('day02/test.data','r')

# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
goal = {'red':12,'green':13,'blue':14}
possible_games = []
for line in [l.strip() for l in file]:
    bag = {'red':0,'green':0,'blue':0}
    (game, handfuls) = [x.strip() for x in line.split(":")]
    game_id = int(game.split(' ')[1])

    for handful in handfuls.split(';'):
        for (n, colour) in [c.strip().split(' ') for c in handful.split(',')]:
            bag[colour] = max(bag[colour], int(n))
    
    print(handfuls)
    print(bag)
    if bag['red'] <= goal['red'] and \
       bag['green'] <= goal['green'] and \
       bag['blue'] <= goal['blue']:
        possible_games.append(game_id)

pp.pprint(possible_games)
print(sum(possible_games))