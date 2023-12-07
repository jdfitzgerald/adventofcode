import pprint
pp = pprint.PrettyPrinter(indent=2)

def bucket_hand(hand) -> int:
    c = [(x, hand.count(x)) for x in set(hand)]
    c.sort(key=lambda x: x[1], reverse=True)
    if c[0][1] == 5:
        return 6
    elif c[0][1] == 4:
        return 5
    elif c[0][1] == 3 and c[1][1] == 2:
        return 4
    elif c[0][1] == 3:
        return 3
    elif c[0][1] == 2 and c[1][1] == 2:
        return 2
    elif c[0][1] == 2:
        return 1
    return 0

file = open('day07/real.data','r')
#file = open('day07/test.data','r')
buckets = [[],[],[],[],[],[],[]]
for (hand, bid) in [l.strip().split() for l in file]:
    buckets[bucket_hand(hand)].append((hand, int(bid)))

rank = "AKQJT98765432"[::-1]

"""
test = ["T55J5","QQQJA","KK677","KTJJT"]
test = sorted(test,key=lambda x: [rank.rfind(c) for c in x])
print(test)
"""

mutliplier = 1
total = 0
for i in range(0,7):
    if len(buckets[i]) == 0:
        continue
    bucket = sorted(buckets[i], key=lambda x: [rank.rfind(c) for c in x[0]])
    for (hand, bid) in bucket:
        total += bid*mutliplier
        mutliplier += 1

print(total)