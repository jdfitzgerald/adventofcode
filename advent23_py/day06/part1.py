import pprint
pp = pprint.PrettyPrinter(indent=2)


file = open('day06/real.data','r')
#file = open('day06/test.data','r')

times = [int(x) for x in file.readline().strip().split()[1::]]
records = [int(x) for x in file.readline().strip().split()[1::]]

total_wins = 1
for (race_num,time) in enumerate(times):
    winners = 0
    for i in range(1,time):
        if i*(times[race_num]-i) > records[race_num]:
            winners += 1
    total_wins *= winners

print(total_wins)
