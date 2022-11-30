import pprint 
pp = pprint.PrettyPrinter(indent=2)

# test
#t = { 'x_min':20, 'x_max':30, 'y_min':-10, 'y_max':-5 }
# data
t = { 'x_min':56, 'x_max':76, 'y_min':-162, 'y_max':-134 }

t['x_range'] = range(t['x_min'], t['x_max']+1)
t['y_range'] = range(t['y_min'], t['y_max']+1)


def check_hit(vx, vy):
	(x,y) = (0,0)

	path = []
	path.append((x,y))
# skip if we'll never reach it
	if (vx**2+vx)/2 < t['x_min']: return (False,path)

	while y > t['y_min'] and x < t['x_max']:
		(x,y) = (x+vx,y+vy)
		path.append((x,y))
		if x in t['x_range'] and y in t['y_range']: return (True,path)
		if vx > 0: vx -= 1
		elif vx < 0: vx += 1
		vy -= 1

	return (False,path)

		
pp.pprint(t)

min_vx = int(t['x_min']**0.5)  # close enough
max_vx = t['x_max']
min_vy = t['y_min']
max_vy = 1000

solns = []
for vx in range(min_vx, max_vx+1):
	for vy in range(min_vy,max_vy):
		(hit, path) = check_hit(vx,vy)
		if hit:
			solns.append((vx,vy))
			print(vx,vy,max([y for (x,y) in path]))

print(len(solns))
