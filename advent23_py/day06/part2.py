import pprint
pp = pprint.PrettyPrinter(indent=2)


file = open('day06/real.data','r')
#file = open('day06/test.data','r')

time = int(''.join(file.readline().strip().split()[1::]))
record = int(''.join(file.readline().strip().split()[1::]))

winners = 0
for i in range(1,time):
    if i*(time-i) > record:
        winners += 1

print(winners)
