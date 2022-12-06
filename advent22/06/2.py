import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

for line in [l.strip() for l in file]:
    for i in range(len(line)-14):
        if len(set(line[i:i+14])) == 14:
            print(i+14)
            break
    
