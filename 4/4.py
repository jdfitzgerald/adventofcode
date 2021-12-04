import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

lines = []

v = [[],[],[],[],[]]

for lnum,l in enumerate(file):
	l = l.strip()
	if lnum > 1:
		if l=='':
			lines += v
			v = [[],[],[],[],[]]
		else:
			a = [int(x) for x in l.split()]
			lines.append(a)
			for i in range(5):
				v[i].append(a[i])

	elif lnum==0:
		nums = [int(x) for x in l.split(',')]

lines += v

lines = [set(x) for x in lines]

for x in nums:
	skip_to=0
	lines_cp = [l for l in lines]
	for i,line in enumerate(lines):
		if skip_to > i:
			continue

		line.discard(x)
		if len(line) == 0:
			start_index = i-i%10

			totes = 0
			for j in range(5):
				totes += sum(lines[start_index+j])

			print('score for last card %d %d = %d'%(totes,x,totes*x))
			start = i-i%10
			skip_to = start + 10
			del(lines_cp[start:start+10])

	if len(lines_cp) > 0:
		lines = lines_cp
		lines = [l for l in lines_cp]
	else:
		break

