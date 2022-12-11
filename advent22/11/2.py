import pprint 
import collections as c
import re

pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

items = []
operations = []
mods = []
trues = []
falses = []

monkeys = []

max_modulo = 1
for line in [l.strip() for l in file if l.strip() != '']:
    if line[0] == 'M':
        monkey = {'id':len(monkeys)}
        monkeys.append(monkey)
    elif line[0] == 'S':
        monkey['items']=c.deque([int(x) for x in line[16:].split(', ')])
    elif line[0] == 'O':
        monkey['op'] = eval('lambda old: ' + line[17:])
    elif line[0] == 'T': 
        monkey['test']=int(line[18:])
        max_modulo *= monkey['test']
    elif line[3] == 't': monkey['true']=int(line[25:])
    elif line[3] == 'f': monkey['false']=int(line[26:])
    else: print(line)


activity=[0 for x in range(len(monkeys))]
for i in range(10000):
    for monkey in monkeys:
        while (len(monkey['items'])):
            activity[monkey['id']] += 1
            item = monkey['items'].popleft()
            worry = monkey['op'](item) % max_modulo
            if worry % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(worry)
            else:
                monkeys[monkey['false']]['items'].append(worry)


activity.sort(reverse=True)

print(activity[0]*activity[1])
