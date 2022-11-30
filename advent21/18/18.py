import pprint 
pp = pprint.PrettyPrinter(indent=2)

class Node:
	def __init__(self,depth=0,parent=None,val=None):
		self.depth = depth
		self.parent = parent
		self.val = val
	
	@classmethod
	def from_list(cls, init, depth=0, parent=None):
		node = Node(depth, parent)

		if type(init) is int:
			node.val = init
		else:
			[left,right] = init
			node.left = Node.from_list(left,depth+1,node)
			node.right = Node.from_list(right,depth+1,node)

		return node

	@classmethod
	def from_string(cls, string):
		l = eval(string)
		return cls.from_list(l)

	
	def as_string(self):
		if self.val is not None: 
			return '%d'%self.val
		else: 
			return '[%s, %s]'%(self.left.as_string(), self.right.as_string())
	
	def get_descendents(self,all_nodes=None):
		if all_nodes is None: all_nodes = []
		all_nodes.append(self)
		if self.val is None:
			self.left.get_descendents(all_nodes)
			self.right.get_descendents(all_nodes)
		return all_nodes

	def get_magnitude(self):
		if self.val is not None: return self.val
		else: return 3*self.left.get_magnitude() + 2*self.right.get_magnitude()
	

def explode(all_nodes):
	rcarry = 0
	lneighbour = None

	nit = iter(all_nodes)
	node = next(nit,False)
	while node:
		if node.depth==4 and node.val is None and rcarry == 0:
			if lneighbour is not None: 
				lneighbour.val += node.left.val
			rcarry = node.right.val
			all_nodes.remove(node.left)
			all_nodes.remove(node.right)
			node.left = None
			node.right = None
			node.val = 0
			lneighbour = node
			node = next(nit,False)
			continue

		if node.val is not None: 
			lneighbour = node
			if rcarry > 0:
				node.val += rcarry
				rcarry = 0
				return True


		node = next(nit,False)
	return False

def split(all_nodes):
	for n in all_nodes:
		if n.val and n.val >= 10:
			n.left = Node(n.depth+1, n, n.val//2)
			n.right = Node(n.depth+1, n, n.val - n.left.val)
			n.val = None
			return True
	return False

def reduce(root_node):
	loop_again = True
	while loop_again:
		all_nodes = root_node.get_descendents()
		loop_again = explode(all_nodes)
		if loop_again: continue
		loop_again = split(all_nodes)


#file = open('test','r')
file = open('data','r')

root_node = None
for line in file:
	if root_node is None:
		root_node = Node.from_string(line.strip())
	else: 
		string = "[%s,%s]"%(root_node.as_string(),line.strip())
		root_node = Node.from_string(string)

	
	print('*', root_node.as_string())
	reduce(root_node)
	print('-', root_node.as_string())
	print('******')

print(root_node.get_magnitude())
