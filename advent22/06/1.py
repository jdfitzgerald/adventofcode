import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

for line in [l.strip() for l in file]:
    for i in range(len(line)-4):
        if len(set(line[i:i+4])) == 4:
            print(i+4)
            break
