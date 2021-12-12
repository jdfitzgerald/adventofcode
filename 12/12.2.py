import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test3','r')
file = open('data','r')

graph = {}

def add_edge(a,b):
	if a not in graph: graph[a] = []
	if b not in graph: graph[b] = []
	graph[a].append(b)
	graph[b].append(a)

for line in file:
	add_edge(*line.strip().split('-'))

paths = []
def find_paths(node,visited=[],double_done=False):
	visited.append(node)

	if node == 'end': 
		paths.append(visited)
		return

	for n in graph[node]:
		if n not in visited or n.isupper():
			find_paths(n, visited.copy(), double_done)
		elif n not in ['start','end'] and double_done is False:
			find_paths(n, visited.copy(), True)
	
find_paths('start')
pp.pprint(len(paths))
