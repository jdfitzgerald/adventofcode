import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

"""
grid = []
for y, line in enumerate(file):
	grid.append([int(c) for c in line.strip()])

pp.pprint(grid)
max_x = len(grid[0])-1
max_y = len(grid)-1


"""

costs = {(x,y):int(cost) for y, line in enumerate(file) for x,cost in enumerate(line.strip())}

(max_x,max_y) = list(costs.keys())[-1]

paths = {}
unvisited_nodes = []

import sys
for node in costs:
    paths[node]=sys.maxsize
    unvisited_nodes.append(node)


def get_neighbours(node):
    global max_x, max_y
    neighbours = [node for node in [
            (node[0]-1, node[1]),
            (node[0]+1, node[1]),
            (node[0], node[1]-1),
            (node[0], node[1]+1)
            ] if node[0] in range(0,max_x+1) and node[1] in range(0,max_y+1)]
    return neighbours

costs[(0,0)] = 0
paths[(0,0)] = 0


while len(unvisited_nodes) > 0:
    cur_node = min({k:paths[k] for k in unvisited_nodes}, key=paths.get)

    unvisited_nodes.remove(cur_node)
    for node in get_neighbours(cur_node):
        paths[node] = min(paths[node], paths[cur_node]+costs[node])

print(paths[(max_x,max_y)])
