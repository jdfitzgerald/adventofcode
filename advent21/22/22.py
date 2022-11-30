import re
import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test2','r')
#file = open('data','r')

regex="^(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
#regex="^(on|off) x=(-?\d+)..(-?\d+),"


core = {}
def turnon(x,y,z):
    core[(x,y,z)] = 1
    
def turnoff(x,y,z):
    core.pop((x,y,z),None)

# bounds are -50..50
def out_of_bounds(x1,x2,y1,y2,z1,z2):
    if x2 < -50 or y2 < -50 or z2 < -50 or x1 > 50 or y1 > 50 or z1 > 50: return True
    else: return False

for line in file:
    print(line)
    match = re.findall(regex,line)[0]
    cmd = match[0]
    (x1,x2,y1,y2,z1,z2) = [int(n) for n in match[1:]]

    if out_of_bounds(x1,x2,y1,y2,z1,z2): 
        print('ooob')
        continue

    if cmd == 'on':
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    turnon(x,y,z)
    elif cmd == 'off':
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    turnoff(x,y,z)


print(len(core))
