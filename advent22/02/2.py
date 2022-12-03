import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

ROCK='rock'
PAPER='paper'
SCISSORS='scissors'
LOSE=0
DRAW=3
WIN=6

mapping = {}
mapping['A'] = ROCK
mapping['B'] = PAPER
mapping['C'] = SCISSORS

mapping['X'] = LOSE
mapping['Y'] = DRAW
mapping['Z'] = WIN

strategies = {}
strategies[ROCK] = {LOSE: SCISSORS, DRAW: ROCK, WIN: PAPER}
strategies[PAPER] = {LOSE: ROCK, DRAW: PAPER, WIN: SCISSORS}
strategies[SCISSORS] = {LOSE: PAPER, DRAW: SCISSORS, WIN: ROCK}

pp.pprint(strategies)
scores={}
scores[ROCK]=1
scores[PAPER]=2
scores[SCISSORS]=3

def score_game(opp, me):
    score = scores[me]
    if opp == me: return score+DRAW
    elif opp == ROCK and me == PAPER: return score+WIN
    elif opp == SCISSORS and me == ROCK: return score+WIN
    elif opp == PAPER and me == SCISSORS: return score+WIN
    else: return score+LOSE

total_score = 0
for [opp_code, strat_code] in [l.strip().split() for l in file]:
    opp = mapping[opp_code]
    strat = mapping[strat_code]
    score = score_game(opp, strategies[opp][strat])
    print(score)
    total_score += score
    
print(total_score)
