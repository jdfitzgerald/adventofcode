import pprint 
import os 
pp = pprint.PrettyPrinter(indent=2)


#file = open(os.path.dirname(__file__)+'/real.data','r')
file = open(os.path.dirname(__file__)+'/test.data','r')
for line in [l.strip() for l in file]:
    pp.pprint(line)