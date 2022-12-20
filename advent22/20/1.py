import pprint 
import os 

pp = pprint.PrettyPrinter(indent=2)

#filename = os.path.dirname(__file__)+'/test'
filename = os.path.dirname(__file__)+'/data'

class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class DLList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, val):
        self.length += 1
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            new_node.prev = self.head
            new_node.next = self.head
        else:
            self.insert(self.head.prev, new_node)

    def print(self):
        node = self.head.next
        print(self.head.val, end=' ')
        while node != self.head:
            print(node.val, end=' ')
            node = node.next
        print('')

    def encrypt(self):
        queue = []
        node = self.head
        while len(queue) < self.length:
            queue.insert(0,node)
            node = node.next

        while len(queue) > 0:
            move_node = queue.pop()
            target = move_node
            steps = abs(move_node.val)%self.length
            if move_node.val < 0: steps += 1
            if steps != 0:
                for i in range(steps):
                    target = target.prev if move_node.val < 0 else target.next
                self.remove(move_node)
                self.insert(target,move_node)
            

    def remove(self,node):
        if node == self.head:
            self.head = node.next
        node.prev.next=node.next
        node.next.prev=node.prev
        node.next = None
        node.prev = None

    def insert(self,target,move_node):
        move_node.prev = target
        move_node.next = target.next
        move_node.next.prev = move_node
        target.next = move_node

    def find_by_val(self,val):
        node = self.head
        while node is not None:
            if node.val == val:
                return node
            node = node.next
            if node == self.head:
                return None

    def find_by_steps(self, node, steps):
        for i in range(steps):
            node = node.next
        return node



file = open(filename,'r')

nlist = DLList() 
for line in [l.strip() for l in file]:
    nlist.append(int(line))

nlist.encrypt()
zero_node = nlist.find_by_val(0)

node1 = nlist.find_by_steps(zero_node,1000)
node2 = nlist.find_by_steps(node1,1000)
node3 = nlist.find_by_steps(node2,1000)

nlist.print()
print(node1.val,node2.val,node3.val,node1.val+node2.val+node3.val)
