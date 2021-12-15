import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

folds = []
dots = {}

max_x = 0
max_y = 0

def add_dot(x,y):
	print('add dot %d %d'%(x,y))
	if y not in dots: dots[y] = set()
	dots[y].add(x)
	global max_x
	max_x = max(max_x, x)

for line in file:
	if line[:4] == 'fold':
		folds.append(line.strip().split()[2].split('='))
	elif line.strip() != '':
		add_dot(*[int(x) for x in line.strip().split(',')])

pp.pprint(dots)

max_y = max(dots.keys())

for fold in folds:
	fold_index = int(fold[1])
	if fold[0] == 'x':
		for y in list(dots):
			for x in list(dots[y]):
				if x>=fold_index:
					add_dot(2*fold_index-x,y)
					dots[y].discard(x)
		max_x = fold_index -1

	else:
		for y in list(dots):
			if y>=fold_index:
				for x in list(dots[y]):
					add_dot(x,2*fold_index-y)
				del dots[y]
		max_y = fold_index -1

for y in range(0, max_y+1):
	for x in range(0, max_x+1):
		if x in dots[y]: print('#',end='')
		else: print('.',end='')
	print()
