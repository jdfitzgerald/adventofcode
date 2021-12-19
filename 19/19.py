import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
file = open('data','r')

MAX_SCAN=80 # limit for testing
scan_data = []
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

pp.pprint(len(relative_distances))


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
		
pp.pprint(potential_matches)

sdp = 0
for (a,b) in potential_matches:
	distinct_points = len(set([x for (x,y) in potential_matches[(a,b)]]))
	sdp += distinct_points
	if distinct_points < 12:
		print(a,b,'not a match',distinct_points)
	else:
		pp.pprint(potential_matches[(a,b)])

