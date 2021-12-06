import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

l = file.readline()
fish = [int(t) for t in l.split(',')]

for d in range(80):
	fish = [t-1 for t in fish]
	new_fish = [8 for t in fish if t == -1]
	fish = [6 if t == -1 else t for t in fish]
	fish += new_fish

print(len(fish))
