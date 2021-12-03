file = open('test','r')
#file = open('data','r')

x=0

for index,line in enumerate(file):
	v=line.strip()
	#n = int(v, 2)

	if index==0: 
		totals=[]
		for i in range(len(v)):
			totals.append(0)

	for i in range(len(v)):
		totals[i] = totals[i] + int(v[i])
	print(totals)

target = index/2
gamma = ''
epsilon = ''
for t in totals:
	if t > target:
		gamma+='1'
		epsilon+='0'
	else:
		gamma+='0'
		epsilon+='1'

power = int(gamma, 2) * int(epsilon,2)
print(gamma, epsilon)
print(power)

