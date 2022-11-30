total = 0	
for line in open('data','r'):
	bylength = {2:[],3:[],4:[],5:[],6:[],7:[]}
	(nums,vals) = [x.split() for x in line.strip().split(' | ')]

	for n in nums:
		bylength[len(n)].append(set(list(n)))

	one = bylength[2][0]
	seven = bylength[3][0]
	four = bylength[4][0]
	eight = bylength[7][0]
# intersections
	i235 = (bylength[5][0] & bylength[5][1] & bylength[5][2])
	i069 = (bylength[6][0] & bylength[6][1] & bylength[6][2])

	a = seven - one
	g = i235 - a - four
	d = i235 - one - a - g
	b = i069 - a - g - one
	f = i069 - a - g - b
	c = one - f
	e = eight - four - a - g

	mapping = {}
	mapping[''.join(sorted(a|b|c|e|f|g))] = 0
	mapping[''.join(sorted(one))] = 1
	mapping[''.join(sorted(a|c|d|e|g))] = 2
	mapping[''.join(sorted(a|c|d|f|g))] = 3
	mapping[''.join(sorted(b|c|d|f))] = 4
	mapping[''.join(sorted(a|b|d|f|g))] = 5
	mapping[''.join(sorted(a|b|d|e|f|g))] = 6
	mapping[''.join(sorted(seven))] = 7
	mapping[''.join(sorted(eight))] = 8
	mapping[''.join(sorted(a|b|c|d|f|g))] = 9

	number = 0

	for i,v in enumerate(vals):
		magnitude = 10**(len(vals) - i -1)
		number += magnitude * mapping[''.join(sorted(v))]
	
	total += number

print(total)

