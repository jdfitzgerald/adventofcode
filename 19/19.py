import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
SCANNERS = 5
file = open('data','r')
SCANNERS = 26

routes = []
for i in range(SCANNERS): routes.append([])

print('*******************')
print('*******************')

scan_data = []

combos = ['xyz','xzy','yxz','yzx','zxy','zyx']
multipliers = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
variations = [(m,c) for m in multipliers for c in combos]

scanner = 0
total_beacons = 0
for line in file:
	if line[0:3]=='---': 
		scanner = int(line.strip().split()[2])
		scan_data.append([])
		continue
	elif line.strip():
		total_beacons += 1
		point=tuple([int(i) for i in line.strip().split(',')])
		scan_data[scanner].append(point)

all_beacons = scan_data[0]

from collections import defaultdict
relative_distances = defaultdict(list)
for scanner in range(0,len(scan_data)):
	for ibeacon in range(0,len(scan_data[scanner])-1):
		for jbeacon in range(ibeacon+1,len(scan_data[scanner])):
			a = scan_data[scanner][ibeacon]
			b = scan_data[scanner][jbeacon]
			d = ((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2)**0.5
			relative_distances[d].append((scanner,scan_data[scanner][ibeacon],scan_data[scanner][jbeacon]))


potential_matches = defaultdict(set)
for d in relative_distances:
	pointlist = relative_distances[d]
	while len(pointlist) >= 1:
		point = pointlist[0]
		pointlist = pointlist[1:]
		for p in pointlist:
			if p[0] != point[0]: 
				potential_matches[(point[0],p[0])].add((point[1],p[1]))
				potential_matches[(point[0],p[0])].add((point[2],p[2]))
		

def transform_x(point, translation, varient):
	res = ( 
		point[0] + translation[varient[1].index('x')]*varient[0][0],
		point[1] + translation[varient[1].index('y')]*varient[0][1],
		point[2] + translation[varient[1].index('z')]*varient[0][2]
		)
	return res

def add(origin, point, varient):
	res = ( 
		origin[0] + point[varient[1].index('x')]*varient[0][0],
		origin[1] + point[varient[1].index('y')]*varient[0][1],
		origin[2] + point[varient[1].index('z')]*varient[0][2]
		)
	return res

# diff points with remapping
def sub(A, B, varient):
	res = ( 
		A[0] - B[varient[1].index('x')]*varient[0][0],
		A[1] - B[varient[1].index('y')]*varient[0][1],
		A[2] - B[varient[1].index('z')]*varient[0][2]
		)
	return res

# used to go the opposite way to the varient
def backtrack(point, transform):
	n = variations[0] #neutral
	t_rev = ([-x for x in transform[1][0]],transform[1][1]) # reverse transform
	res = sub(transform[0],point,n)
	return add((0,0,0),res,t_rev)

def fronttrack(point, transform):
	return add(transform[0],point,transform[1])

def find_scanner_transform(matches):
	working=defaultdict(set)
	for (k,v) in matches: working[k].add(v)

	latest = None
# grab two points with the least matching points, so most likely right?
	((_,first),(_,second)) = sorted([(len(working[k]),k) for k in working])[0:2]
	for point in working[first]: 
		for v in variations: # cycle through orientations
			d = sub(first,point,v)
			for op in working[second]:
				if second == add(d,op,v):
					latest = (d,v)
# this is janky, should really verify which is correct
	return latest
transformers = {}

for (a,b) in potential_matches:
	distinct_points = len(set([x for (x,y) in potential_matches[(a,b)]]))
	if distinct_points >= 12:
		trans = find_scanner_transform(potential_matches[(a,b)])
		if trans is not None:
			#if (b,a) == (4,1): pp.pprint(potential_matches[(a,b)])
			routes[a].append(b)
			routes[b].append(a)
			transformers[(b,a)] = trans

		print('a,b relative loc', a,b,trans)

"""
for k,route in enumerate(routes):
	print(k,route)
	"""

operations = [(2,4),(4,1),(3,1),(1,0)]

"""
debug of points for 4-1-0 in test
debug_points = [ (515, 917, -361), (-340, -569, -846), (-460, 603, -452), (-466, -666, -811), (-355, 545, -477), (703, -491, -529), (413, 935, -424), (-391, 539, -444), (-364, -763, -893), (807, -499, -711), (755, -354, -619), (553, 889, -390), (515, 917, -361), (-466, -666, -811), (515, 917, -361), (-340, -569, -846), (-466, -666, -811), (703, -491, -529), (-364, -763, -893), (807, -499, -711), (755, -354, -619)]
"""

for op in operations:
	(src,dst) = op
	if op not in transformers:
		method = backtrack
		transform = transformers[(dst,src)]
	else: 
		method = fronttrack
		transform = transformers[op]
		
	for point in scan_data[src]:
		np = method(point,transform)
		scan_data[dst].append(np)
		if np in debug_points or point in debug_points:
			print(method, op, point, np)

pp.pprint(set(scan_data[0]))
print(len(scan_data[0]))
print(len(set(scan_data[0])))


