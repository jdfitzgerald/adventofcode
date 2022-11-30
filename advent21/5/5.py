import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
#file = open('data','r')

hits = {}

def add_hit(x,y):
	if x not in hits:
		hits[x]={}
	if y not in hits[x]:
		hits[x][y]=0
	hits[x][y]+=1


for line_num, line in enumerate(file):
	coords = line.split(' -> ')
	coords[0] = [int(i) for i in coords[0].split(',')]
	coords[1] = [int(i) for i in coords[1].split(',')]

	if (coords[0][0] == coords[1][0]):
		x=coords[0][0]
		end=max(coords[0][1],coords[1][1])
		start=min(coords[0][1],coords[1][1])
		for y in range(start, end+1):
			add_hit(x,y)

	elif (coords[0][1] == coords[1][1]):
		y=coords[0][1]
		end=max(coords[0][0],coords[1][0])
		start=min(coords[0][0],coords[1][0])
		for x in range(start, end+1):
			add_hit(x,y)


l=len([i for col in hits.values() for i in col.values() if i>1])
pp.pprint(l)

