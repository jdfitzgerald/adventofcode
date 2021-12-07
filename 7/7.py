import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
file = open('data','r')

line = file.readline()
crabs = [int(x) for x in line.strip().split(',')]

max_pos = max(crabs)+1;
costs=[0]*max_pos
for pos in range(max_pos):
	for crab in crabs:
		costs[pos] += abs(pos - crab)

print(min(costs), costs.index(min(costs)))
	

