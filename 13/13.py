import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
#file = open('data','r')

folds = []
dots = {}

max_x = 0
max_y = 0

def add_dot(x,y):
	if y not in dots: dots[y] = {}
	dots[y][x] = 1 
	print(x,y,max_x)
	max_x = max(max_x,x)

for line in file:
	if line[:4] == 'fold':
		folds.append(line.strip().split()[2].split('='))
	elif line.strip() != '':
		add_dot(*[int(x) for x in line.strip().split(',')])

max_y = max(dots.keys())

print(max_x,max_y)


for fold in folds:
	fold_index = int(fold[1])
	if fold[0] == 'y':
		for y in dots:
			if y > fold_index:
				print(y)
