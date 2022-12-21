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

    def update_vals(self, name, val):
        if name == self.left:
            self.left = val
        if name == self.right:
            self.right = val
        if not isinstance(self.right, str) and not isinstance(self.left, str):
            v = eval('%d %s %d'%(self.left,self.op,self.right))
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


monkey_tree = MonkeyTree()

for line in [l.strip() for l in file]:
    (name, op) = line.split(': ')
    monkey_tree.add_monkey(name, op)

monkey_tree.resolve()

print(monkey_tree.monkeys['root'].val)