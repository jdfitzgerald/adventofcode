import pprint 
import os 
import re 
from collections import deque 

pp = pprint.PrettyPrinter(indent=2)


file = open(os.path.dirname(__file__)+'/real.data','r')
#file = open(os.path.dirname(__file__)+'/test.data','r')


workflows = {}

for line in [l.strip() for l in file]:
    if line == '':
        break
    matches = re.match(r'(\w+){(.*)}',line)
    name = matches.group(1)
    rules = []
    for r in matches.group(2).split(','):
        if ':' in r:
            rules.append({
                'k': r[0],
                'op': r[1],
                'v': int(r[2:].split(':')[0]),
                'action': r[3:].split(':')[1],
            })
        else:
            rules.append({
                'action':r
            })
    workflows[name] = rules

workflows['A'] = [{'action':'A'}]
workflows['R'] = [{'action':'R'}]


def find_accept_paths(workflow, ranges):
    r = list(ranges)
    for rule in workflow:
        # pick each branch
        if 'op' in rule:
            idx = range_map[rule['k']]
            (low, high) = r[idx]
            break_value = rule['v']
            if rule['op'] == '>':
                r[idx] = (max(low, break_value+1), high) #above
                find_accept_paths(workflows[rule['action']], tuple(r))
                r[idx] = (low, min(high, break_value)) #below - continue with this range
            else:
                r[idx] = (low, min(high, break_value-1)) #below
                find_accept_paths(workflows[rule['action']], tuple(r))
                r[idx] = (max(low, break_value), high) #above - continue with this range
        elif rule['action'] == 'A':
            winning_ranges.append(tuple(r))
        elif rule['action'] != 'R':
            find_accept_paths(workflows[rule['action']], tuple(r))


# xmas
ranges = ((1,4000), (1,4000), (1,4000), (1,4000))
range_map = {'x':0, 'm':1, 'a':2, 's':3}
winning_ranges = []
find_accept_paths(workflows['in'], ranges)
pp.pprint(winning_ranges)

total = 0
for r in winning_ranges:
    rtot = 1 
    for p in r:
        rtot *= 1+p[1] - p[0] # off by one error for some reason. +1 magic number fix yay!
    total += rtot
print(total)
