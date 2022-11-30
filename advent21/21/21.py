import pprint 
import itertools
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
#file = open('data','r')

totals = [0,0]
spaces = [10,1]

dice = itertools.cycle([x for x in range(1,101)])

def dice_rolls():
	while	True:
		roll = next(dice) + next(dice) + next(dice)
		print(roll)
		yield roll

player = 0
board_length = 10

def move(pos,roll):
	pos = (pos + roll - 1) % 10
	return pos + 1

total_rolls = 0
for roll in dice_rolls():
	total_rolls += 3
	spaces[player] = move(spaces[player], roll)
	totals[player] += spaces[player]
	print(roll,':',spaces[player],totals[player])
	if totals[player] >= 1000:
		print(player,'is winner after',total_rolls)
		print(totals)
		break
	player = (player + 1)%2

loser = (player + 1)%2
print(totals[loser]*total_rolls)




"""
for n in range(33):
	x = next(roll_dice())
	print(x)

"""
