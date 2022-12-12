import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

graph = []

targets = []
for (i,line) in enumerate([l.strip() for l in file]):
    graph.append([])
    for (j,c) in enumerate(line):
        if c == 'S' or c == 'a':
            targets.append((i,j))
            c = 'a'
        elif c == 'E':
            end = (i,j)
            c = 'z'
        e = ord(c) - 96
        n = []
        if i-1 >= 0:
            if graph[i-1][j]['elev'] in [e-1, e, e+1]: 
                n.append((i-1,j))
                graph[i-1][j]['neigh'].append((i,j))
            elif graph[i-1][j]['elev'] > e:
                n.append((i-1,j))
            else:
                graph[i-1][j]['neigh'].append((i,j))
        if j-1 >= 0:
            if graph[i][j-1]['elev'] in [e-1, e, e+1]: 
                n.append((i,j-1))
                graph[i][j-1]['neigh'].append((i,j))
            elif graph[i][j-1]['elev'] > e:
                n.append((i,j-1))
            else:
                graph[i][j-1]['neigh'].append((i,j))


        graph[i].append({'elev':e,'neigh':n})

unvisited = [(i,j) for i in range(len(graph)) for j in range(len(graph[0]))]

shortest_path = {}
previous_nodes = {}
max_val = 9999999

for node in unvisited:
    shortest_path[node] = max_val

shortest_path[end] = 0

while unvisited:
    cur_min_node = None
    for node in unvisited:
        if cur_min_node == None:
            cur_min_node = node
        elif shortest_path[node] < shortest_path[cur_min_node]:
            cur_min_node = node

    for n in graph[cur_min_node[0]][cur_min_node[1]]['neigh']:
        t = shortest_path[cur_min_node] + 1
        if t < shortest_path[n]:
            shortest_path[n] = t
            previous_nodes[n] = cur_min_node
    unvisited.remove(cur_min_node)


print(min([shortest_path[p] for p in targets]))
