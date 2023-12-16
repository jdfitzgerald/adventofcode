import os 
import pprint 
pp = pprint.PrettyPrinter(indent=2)

def hash(str):
    cv = 0
    for v in [ord(c) for c in str]:
        cv = ((cv + v)*17) % 256
    return cv

file = open(os.path.dirname(__file__)+'/real.data','r')
#file = open(os.path.dirname(__file__)+'/test.data','r')

boxes = [{} for x in range(256)]
boxes_idx = [0 for x in range(256)]

for line in [l.strip() for l in file]:
    for step in line.split(','):
        if step[-1] == '-':
            op = '-'
            label = step[:-1] 
        else:
            fl = step[-1]
            op = '='
            label = step[:-2]

        box_no = hash(label)
        box = boxes[box_no]
        
        if op == '-':
            if label in box:
                del box[label]
        elif label in box:
            box[label]['fl'] = fl
        else:
            idx = boxes_idx[box_no]
            boxes_idx[box_no] += 1
            box[label] = {'fl':fl, 'idx':idx}

total = 0
for (boxno, box) in enumerate(boxes):
    if len(box) == 0:
        continue

    boxno += 1
    slot = 1
    lenses = sorted(box.items(), key=lambda x:x[1]['idx'])

    for (label,lens) in lenses:
        score = boxno * slot * int(lens['fl'])
        slot += 1
        total += score

print(total)