import pprint 
pp = pprint.PrettyPrinter(indent=2)


#file = open('dayXX/real.data','r')
file = open('dayXX/test.data','r')
for line in [l.strip() for l in file]:
    pp.pprint(line)