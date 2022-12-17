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

pp = pprint.PrettyPrinter(indent=2)
filename = os.path.dirname(__file__)+'/test'
#filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')


rex = re.compile(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)")

valves = {}
# build the graph
for line in [l.strip() for l in file]:
    [name, rate, tunnels] = rex.match(line).groups()
    tunnels = tunnels.split(', ')
    valve={'name':name, 'rate':int(rate), 'tunnels':tunnels}
    valves[name] = valve

pp.pprint(valves)

max_score = 0

# depth first based on minutes? Or breadth?
@lru_cache
def stepnscore(ptotal, valve, minutes, onvalves):
    global max_score

    print("At valve %s with ptotal %d and minutes %d" % (valve,ptotal,minutes))
    if minutes <= 1: raise Exception('wtf')

    if minutes == 2: 
        if valve not in onvalves:
            return ptotal+valves[valve]['rate']
        else:
            return ptotal
    max_poss = max_remaining_pressure(onvalves, minutes)

    if max_poss == 0:
        return ptotal

    if ptotal + max_poss < max_score:
        return ptotal
    
    phere = valves[valve]['rate'] * (minutes-1)
    pressures = []

    if valve not in onvalves and minutes > 3 and phere > 0:
        onvalves1 = tuple(sorted(onvalves + (valve,)))
        for next_valve in valves[valve]['tunnels']:
            p = stepnscore(ptotal+phere, next_valve, minutes-2, onvalves1)
            pressures.append(p)

    for next_valve in valves[valve]['tunnels']:
        p = stepnscore(ptotal, next_valve, minutes-1, onvalves)
        pressures.append(p)
    print("Max pressure of %s is %d" % (valve,max(pressures)))

    score = max(pressures)
    max_score = max(max_score, score)

    return score

mins = 30
print('mins',mins,'result',stepnscore(0,'AA',mins,tuple()))