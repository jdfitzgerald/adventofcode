import pprint 
import re
import os
from functools import lru_cache

@lru_cache
def max_remaining_pressure(onvalves, minutes):
    score = 0
    rates = [v['rate'] for v in valves.values() if v['name'] not in onvalves]
    rates.sort(reverse=True)

    for rate in rates:
        if minutes < 2: break
        score += rate * (minutes -1)
        minutes -= 2

    return score

def cost(a,b):
    queue = [(a,[a])]
    while queue:
        (v,path) = queue.pop()
        for t in valves[v]['tunnels'] - set(path):
            if t == b:
                print("dist from %s to %s is"%(a,b),path)
                return len(path)
            else:
                queue.insert(0,(t,path+[t]))

pp = pprint.PrettyPrinter(indent=2)
filename = os.path.dirname(__file__)+'/test'
#filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')


rex = re.compile(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)")

valves = {}
# build the graph
for line in [l.strip() for l in file]:
    [name, rate, tunnels] = rex.match(line).groups()
    tunnels = set(tunnels.split(', '))
    valve={'name':name, 'rate':int(rate), 'tunnels':tunnels}
    valves[name] = valve

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

quit()
