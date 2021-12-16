import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()

costs = {(x,y):int(cost) for y, line in enumerate(file) for x,cost in enumerate(line.strip())}

(tx,ty) = list(costs.keys())[-1]

size_x = ((tx+1) * 5)
size_y = ((ty+1) * 5)

for y in range(0,size_y):
    if y > ty:
        for x in range(0,tx+1):
            costs[(x,y)] = 1+(costs[(x,y-ty-1)])%9
    for x in range(tx+1,size_x):
        costs[(x,y)] = 1+(costs[(x-tx-1,y)])%9

"""
for y in range(0,size_y):
    print(y, end=':')
    for x in range(0,size_x):
        print(costs[(x,y)], end='')
    print()
"""



paths = {}
unvisited_nodes = []

import sys
for node in costs:
    paths[node]=sys.maxsize
    unvisited_nodes.append(node)


def get_neighbours(node):
    global size_x,size_y
    neighbours = [node for node in [
            (node[0]-1, node[1]),
            (node[0]+1, node[1]),
            (node[0], node[1]-1),
            (node[0], node[1]+1)
            ] if node[0] in range(0,size_x) and node[1] in range(0,size_y)]
    return neighbours

costs[(0,0)] = 0
paths[(0,0)] = 0


breaker = 0
def get_min_node():
    cur_node = unvisited_nodes[0]
    for node in unvisited_nodes:
        if paths[node] < paths[cur_node]: cur_node = node
    return cur_node

while len(unvisited_nodes) > 0:
    print(len(unvisited_nodes))
    #cur_node = min({k:paths[k] for k in unvisited_nodes}, key=paths.get)
    cur_node = get_min_node()

    unvisited_nodes.remove(cur_node)
    for node in get_neighbours(cur_node):
        paths[node] = min(paths[node], paths[cur_node]+costs[node])

    breaker +=1 
    if breaker>50: break

print(paths[(size_x-1,size_y-1)])


pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())




