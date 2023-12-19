import pprint 
import os 
import re 

pp = pprint.PrettyPrinter(indent=2)


file = open(os.path.dirname(__file__)+'/real.data','r')
#file = open(os.path.dirname(__file__)+'/test.data','r')

workflows = {}
parts = []

phase = 0
for line in [l.strip() for l in file]:
    if line == '':
        phase = 1
        continue
    elif phase == 0:
        matches = re.match(r'(\w+){(.*)}',line)
        name = matches.group(1)
        rules = []
        for r in matches.group(2).split(','):
            if ':' in r:
                rules.append({
                    'k': r[0],
                    'op': r[1],
                    'v': r[2:].split(':')[0],
                    'action': r[3:].split(':')[1],
                })
            else:
                rules.append({
                    'action':r
                })
        workflows[name] = rules
    else:
        matches = re.match(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)',line)
        part = {
            'x': matches.group(1),
            'm': matches.group(2),
            'a': matches.group(3),
            's': matches.group(4),
        }
        parts.append(part)

        #parts

accepted_parts = []

workflows['A'] = [{'action':'A'}]
workflows['R'] = [{'action':'R'}]
i = 0
for part in parts:
    i+=1
    workflow = workflows['in']
    stop = 0
    while not stop:
        for rule in workflow:
            if 'op' in rule:
                if eval(part[rule['k']] + rule['op']+rule['v']):
                    workflow = workflows[rule['action']]
                    break
            elif rule['action'] == 'A':
                workflow = 'A'
                accepted_parts.append(part)
                stop = 1
            elif rule['action'] == 'R':
                workflow = 'R'
                stop = 1
            else:
                workflow = workflows[rule['action']]
                break

total = 0
for part in accepted_parts:
    total += sum([int(v) for k,v in part.items()])

print(total)