import pprint 
import re
import os
from functools import lru_cache

def cost(a,b):
    queue = [(a,[a])]
    while queue:
        (v,path) = queue.pop()
        for t in valves[v]['tunnels'] - set(path):
            if t == b:
                return len(path)
            else:
                queue.insert(0,(t,path+[t]))

pp = pprint.PrettyPrinter(indent=2)
#filename = os.path.dirname(__file__)+'/test'
filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')


rex = re.compile(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)")

valves = {}
for line in [l.strip() for l in file]:
    [name, rate, tunnels] = rex.match(line).groups()
    tunnels = set(tunnels.split(', '))
    valve={'name':name, 'rate':int(rate), 'tunnels':tunnels}
    valves[name] = valve

# build the simplified graph
graph = {'AA':{}}
for cur in valves:
    if valves[cur]['rate'] > 0:
        graph[cur] = {}
        for v in graph:
            if v != cur:
                c = cost(v,cur)
                graph[v][cur] = c
                graph[cur][v] = c



pp.pprint(graph)

def stepnscore(curv, minutes, path):
    minutes -= 1
    phere = valves[curv]['rate'] * minutes
    pressures = [[phere,path]]
    for v in graph[curv]:
        if v not in path:
            remain = minutes-(graph[curv][v])
            if remain > 2:
                p = stepnscore(v, remain,path + [curv])
                pressures.append([p[0]+phere,path+[curv]])
    return max(pressures, key=lambda x: x[0])
        
mins = 30
print(stepnscore('AA',mins+1,[]))