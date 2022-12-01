import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

calories=[0]
elf=0

for line in [x.strip() for x in file]:
    if line == '':
        elf += 1
        calories.append(0)
    else:
        calories[elf] += int(line)

print("part 1")
print(max(calories))

print("part 2")
calories.sort(reverse=True)
print(sum(calories[0:3]))
