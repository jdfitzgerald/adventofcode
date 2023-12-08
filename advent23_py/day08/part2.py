import pprint 
pp = pprint.PrettyPrinter(indent=2)

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.loc = None
    def __str__(self):
        return self.loc + ' => ' + self.left + ',' + self.right

def path_gen(path):
    i=0
    l = len(path)
    while True:
        yield path[i%l]
        i+=1

file = open('day08/real.data','r')
#file = open('day08/test.data','r')

path = file.readline().strip()
file.readline()


nodelist = {}
while line := file.readline().strip():
    node = Node()
    (node.loc, children) = line.split(' = ')
    (node.left, node.right) = children[1:-1].split(', ')
    nodelist[node.loc] = node

steps = 0
next_step = path_gen(path)

node = nodelist['AAA']

for dir in next_step:
    steps += 1
    
    if dir == 'L':
        node = nodelist[node.left]
    else:
        node = nodelist[node.right]
    
    if node.loc == 'ZZZ':
        break

print(steps)
