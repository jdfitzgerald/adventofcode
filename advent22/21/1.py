import pprint 
import os 

pp = pprint.PrettyPrinter(indent=2)

#filename = os.path.dirname(__file__)+'/test'
filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')

class Monkey:
    def __init__(self, name, val=None, op=None, left=None, right=None):
        self.name = name
        self.val = val
        self.op = op
        self.left = left
        self.right = right
        self.vleft = None
        self.vright = None

    def update_vals(self, name, val):
        if name == self.left:
            self.vleft = val
        if name == self.right:
            self.vright = val
        if self.vright is not None and self.vleft is not None:
            v = eval('%d %s %d'%(self.vleft,self.op,self.vright))
            self.val=v


class MonkeyTree:
    def __init__(self):
        self.monkeys = {}
        self.mappings = {}

    def add_monkey(self, name, val_or_op=''):
        if val_or_op.isnumeric():
            m = Monkey(name, val=float(val_or_op))
        else:
            left = val_or_op[:4]
            right = val_or_op[-4:]
            operation = val_or_op[5]
            self.add_mapping(name,left)
            self.add_mapping(name,right)

            m = Monkey(name, left=left, right=right, op=operation)
        self.monkeys[name] = m

    def add_mapping(self,name,c):
        if c not in self.mappings:
            self.mappings[c] = [name]
        else:
            self.mappings[c].append(name)


    def resolve(self):
        unchecked = list(self.mappings.keys())
        while len(unchecked) > 0:
            for m in unchecked:
                if self.monkeys[m].val:
                    unchecked.remove(m)
                    for name in self.mappings[m]:
                        self.monkeys[name].update_vals(m,self.monkeys[m].val)

    def find_route(self,m,dest):
        monkey = self.monkeys[m]

        if monkey.left == dest:
            return 'L'
        elif monkey.right == dest:
            return 'R'
        
        if monkey.left is not None:
            path = self.find_route(monkey.left,dest)
            if path is not None:
                return 'L'+path

        if monkey.right is not None:
            path = self.find_route(monkey.right,dest)
            if path is not None:
                return 'R'+path

        return None


mt = MonkeyTree()

for line in [l.strip() for l in file]:
    (name, op) = line.split(': ')
    mt.add_monkey(name, op)

mt.resolve()


route = mt.find_route('root','humn')
print(route)

root = mt.monkeys['root']

if route[0] == 'L':
    node = mt.monkeys[root.left]
    target = root.vright
else:
    node = mt.monkeys[root.right]
    target = root.vleft

for side in route[1:]:
    if side == 'L':
        if node.op == '-':
            target = target + node.vright
        elif node.op == '/':
            target = target * node.vright
        elif node.op == '+':
            target = target - node.vright
        elif node.op == '*':
            target = target / node.vright
        node = mt.monkeys[node.left]
    else:
        if node.op == '-':
            target = node.vleft - target
        elif node.op == '/':
            target = node.vleft/target
        elif node.op == '+':
            target = target - node.vleft
        elif node.op == '*':
            target = target/node.vleft
        node = mt.monkeys[node.right]


print(target)