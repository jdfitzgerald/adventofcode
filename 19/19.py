import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
#file = open('data','r')
print('*******************')
print('*******************')

MAX_SCAN=90 # limit for testing
scan_data = []

combos = ['xyz','xzy','yxz','yzx','zxy','zyx']
multipliers = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
variations = [(m,c) for m in multipliers for c in combos]

scanner = 0
total_beacons = 0
for line in file:
	if line[0:3]=='---': 
		scanner = int(line.strip().split()[2])
		if scanner >= MAX_SCAN: break
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
	if scanner >= MAX_SCAN: break
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

def transform(origin, point, varient):
	res = ( 
		origin[0] + point[varient[1].index('x')]*varient[0][0],
		origin[1] + point[varient[1].index('y')]*varient[0][1],
		origin[2] + point[varient[1].index('z')]*varient[0][2]
		)
	return res

# diff points with remapping
def diff(A, B, varient):
	res = ( 
		A[0] - B[varient[1].index('x')]*varient[0][0],
		A[1] - B[varient[1].index('y')]*varient[0][1],
		A[2] - B[varient[1].index('z')]*varient[0][2]
		)
	return res

def find_scanner_transform(working):
	((_,first),(_,second)) = sorted([(len(working[k]),k) for k in working])[0:2]
	for point in working[first]: 
		for v in variations:
			d = diff(first,point,v)
			for op in working[second]:
				if second == transform(d,op,v):
					return (d,v)

for (a,b) in potential_matches:
	distinct_points = len(set([x for (x,y) in potential_matches[(a,b)]]))
	if distinct_points < 12:
		print(a,b,'not a match',distinct_points)
	else:
		working=defaultdict(set)
# refactor this to dict building later
		for (k,v) in potential_matches[(a,b)]: working[k].add(v)

		trans = find_scanner_transform(working)
		print('a,b relative loc', a,b,trans)
