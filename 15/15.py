import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
#file = open('data','r')

grid = []

for y, line in enumerate(file):
	grid.append([int(c) for c in line.strip()])

pp.pprint(grid)



def min_cost_back(x,y):
	print(x,y)
	if x==0 and y==0: return 0
	elif x==0: return min_cost_back(x,y-1) + grid[y][x]
	elif y==0: return min_cost_back(x-1,y) + grid[y][x]
	else: return min(min_cost_back(x-1,y), min_cost_back(x,y-1)) + grid[y][x]


max_x = len(grid[0])-1
max_y = len(grid)-1

print('grid size',max_x,max_y)

print(min_cost_back(max_x, max_y))
