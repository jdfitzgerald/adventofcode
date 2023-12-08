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
#file = open('day08/test2.data','r')

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


current_nodes = [node for k,node in nodelist.items() if k[2]=='A']

visited = {}
print([node.loc for node in current_nodes])
for dir in next_step:
    hash = ''.join(sorted([node.loc for node in current_nodes]))
    if hash in visited:
        print('loop')
        break
    visited[hash]=1

    steps += 1
    z_count = 0
    for i,node in enumerate(current_nodes):
        if dir == 'L':
            node = nodelist[node.left]
        else:
            node = nodelist[node.right]
    
        if node.loc[2] == 'Z':
            z_count += 1
        current_nodes[i]=node


    if z_count > 1:
        print(''.join(sorted([node.loc for node in current_nodes])), z_count)
    if z_count == len(current_nodes):
        break

print(steps)
