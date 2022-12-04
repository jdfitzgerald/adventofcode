import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

count=0

for [one, two] in [[[int(n) for n in x.split('-')] for x in l.strip().split(',')] for l in file]:
    if len(set(range(one[0], one[1]+1)).intersection(set(range(two[0],two[1]+1)))):
        count+=1

print(count)
