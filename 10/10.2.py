import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
file = open('data','r')

closers = {
	')':('(',3),
	']':('[',57),
	'}':('{',1197),
	'>':('<',25137)
}
openers = {
	'(':1,
	'[':2,
	'{':3,
	'<':4
}

scores = []
for line in file:
	stack = []
	corrupt = False
	for bracket in line.strip():
		if bracket in closers.keys():
			if stack.pop() != closers[bracket][0]:
				corrupt = True
				break;
		else: 
			stack.append(bracket)

	score = 0
	if corrupt == False:
		for b in reversed(stack):
			score *= 5
			score += openers[b]

		scores.append(score)


print(sorted(scores)[int(len(scores)/2)])


		
