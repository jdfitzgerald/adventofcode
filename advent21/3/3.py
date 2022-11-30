file = open('test','r')
file = open('data','r')

x=0

n1=[]
n0=[]
ones=0

v='' 

for index,line in enumerate(file):
	v=line.strip()
	if v[0]=='1':
		n1.append(v)
		ones+=1
	else:
		n0.append(v)

nbits = len(v)
	
if ones >= index/2:
	oxy = n1
	co2 = n0
else:
	oxy = n0
	co2 = n1

for i in range(1,nbits):
	n1=[]
	n0=[]
	ones=0
	for v in oxy:
		if v[i]=='1':
			n1.append(v)
			ones+=1
		else:
			n0.append(v)

	if ones >= len(oxy)/2:
		oxy = n1
	else:
		oxy = n0
	
	if len(oxy) == 1:
		break;

for i in range(1,nbits):
	n1=[]
	n0=[]
	ones=0
	print(co2)
	for v in co2:
		if v[i]=='1':
			n1.append(v)
			ones+=1
		else:
			n0.append(v)

	print(ones, len(co2), n0, n1)
	if ones >= len(co2)/2:
		co2 = n0
	else:
		co2 = n1
	
	if len(co2) == 1:
		break;


print(oxy)
print(co2)
ans = int(oxy[0],2)*int(co2[0],2)

print(ans)
