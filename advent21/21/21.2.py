import pprint 
pp = pprint.PrettyPrinter(indent=2)

spaces = (4,8)
#spaces = [10,1]
wins = [0,0]

possible_rolls = [a+b+c for a in [1,2,3] for b in [1,2,3] for c in [1,2,3]]

player = 0
board_length = 10

import functools
@functools.lru_cache(maxsize=None)
def move(pos,roll):
	pos = (pos + roll - 1) % 10
	return pos + 1

target = 13
def take_turn(p1,t1,p2,t2):
	wins=[0,0]
	for a in possible_rolls:
		p1_n = move(p1,a)
		t1_n = p1 + t1
		if t1_n>=target: wins[0]+=1
		else:
			for b in possible_rolls:
				p2_n = move(p2,b)
				t2_n = p2 + t2
				if t2_n>=target: wins[1]+=1
				else: 
					wins = [a+b for a,b in zip(wins,take_turn(p1_n,t1_n,p2_n,t2_n))]
	return wins


res = take_turn(4,0,8,0)
print(res)
