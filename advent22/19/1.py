import pprint 
import os 
import re

pp = pprint.PrettyPrinter(indent=2)

filename = os.path.dirname(__file__)+'/test'
#filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')

p = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
rex = re.compile(p)

for line in [l.strip() for l in file]:
    (bid, ore_cost_ore, clay_cost_ore, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay) = [int(d) for d in rex.match(line).groups()]
    print(bid, ore_cost_ore, clay_cost_ore, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay)

mins = 24

#This is ratios in factorio?

stockpile = {
    'ore': 0,
    'clay': 0,
    'obsidian': 0,
    'geodes': 0,
    }

rates = {
    'ore': 1,
    'clay': 0,
    'obsidian': 0,
    'geodes': 0,
    }


