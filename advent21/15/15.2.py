import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
file = open('data','r')


costs = {(x,y):int(cost) for y, line in enumerate(file) for x,cost in enumerate(line.strip())}

(tx,ty) = list(costs.keys())[-1]

size_x = ((tx+1) * 5)
size_y = ((ty+1) * 5)

# expand out the grid
for y in range(0,size_y):
    if y > ty:
        for x in range(0,tx+1):
            costs[(x,y)] = 1+(costs[(x,y-ty-1)])%9
    for x in range(tx+1,size_x):
        costs[(x,y)] = 1+(costs[(x-tx-1,y)])%9

paths = {}
visited_nodes = {}

import sys
for node in costs:
    paths[node]=sys.maxsize


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

from heapq import heappush, heappop

unvisited_nodes = [(0,(0,0))]

while len(unvisited_nodes) > 0:
    cur_node = heappop(unvisited_nodes)[1]

    visited_nodes[cur_node]=1

    for node in get_neighbours(cur_node):
        new_cost = paths[cur_node]+costs[node]
        if paths[node] > new_cost:
          if node not in visited_nodes: 
            if (paths[node],node) in unvisited_nodes: unvisited_nodes.remove((paths[node],node))
            heappush(unvisited_nodes,(new_cost,node))
          paths[node] = new_cost

print(paths[(size_x-1,size_y-1)])
