import os 
import pprint 
pp = pprint.PrettyPrinter(indent=2)

def hash(str):
    cv = 0
    for v in [ord(c) for c in str]:
        cv = ((cv + v)*17) % 256
    return cv

#file = open(os.path.dirname(__file__)+'/real.data','r')
file = open(os.path.dirname(__file__)+'/test.data','r')
for line in [l.strip() for l in file]:
    total = 0
    for step in line.split(','):
        cv = hash(step)
        print(step, cv)
        total += cv
    print(total)