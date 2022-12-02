import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

ROCK='rock'
PAPER='paper'
SCISSORS='scissors'

mapping = {}
mapping['A'] = ROCK
mapping['B'] = PAPER
mapping['C'] = SCISSORS
mapping['X'] = ROCK
mapping['Y'] = PAPER
mapping['Z'] = SCISSORS

scores={}
scores[ROCK]=1
scores[PAPER]=2
scores[SCISSORS]=3

def score_game(opp, me):
    win=6
    draw=3
    lose=0

    if opp == me: return draw
    elif opp == ROCK and me == PAPER: return win
    elif opp == SCISSORS and me == ROCK: return win
    elif opp == PAPER and me == SCISSORS: return win
    else: return lose

total_score = 0
for [opp, me] in [[mapping[x] for x in l.strip().split()] for l in file]:
    print(opp,me)
    score = scores[me] + score_game(opp, me)
    print(score)
    total_score += score
    
print(total_score)
