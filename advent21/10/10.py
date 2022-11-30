import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

closers = {
	')':('(',3),
	']':('[',57),
	'}':('{',1197),
	'>':('<',25137)
}

score = 0
for line in file:
	stack = []
	for bracket in line.strip():
		if bracket in closers.keys():
			if stack.pop() != closers[bracket][0]:
				score += closers[bracket][1]
				break;
		else: 
			stack.append(bracket)

print(score)


		
