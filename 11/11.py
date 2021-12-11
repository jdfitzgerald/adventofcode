import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

import functools
grid = [list(map(int, list(line.strip()))) for line in file]
\

def add_one(x,y):
	if x not in range(0,10) or y not in range(0,10): return

	grid[y][x]+=1
	if grid[y][x] == 10:
		add_one(x-1,y-1)
		add_one(x,y-1)
		add_one(x+1,y-1)
		add_one(x-1,y)
		add_one(x,y)
		add_one(x+1,y)
		add_one(x-1,y+1)
		add_one(x,y+1)
		add_one(x+1,y+1)

flashes=0
for step in range(0,100):
	for y in range(0,10):
		for x in range(0,10):
			add_one(x,y)
	
	for y in range(0,10):
		for x in range(0,10):
			if grid[y][x] >= 10:
				flashes+=1
				grid[y][x]=0

pp.pprint(flashes)

