import pprint
import math
pp = pprint.PrettyPrinter(indent=2)

file = open('day04/real.data','r')
#file = open('day04/test.data','r')
total = 0
card_counts = [0]
for line in [l.strip() for l in file]:
    data = line.split(':')
    card_num = int(data[0].split()[1])
    if card_num >= len(card_counts):
        card_counts.append(0)

    card_counts[card_num] += 1

    (winners,numbers) = [set(x.strip().split()) for x in data[1].strip().split('|')]
    for i in range(1,len(winners & numbers)+1):
        if card_num +i >= len(card_counts):
            card_counts.append(0)
        card_counts[card_num+i] += card_counts[card_num]




pp.pprint(card_counts)
pp.pprint(sum(card_counts))
