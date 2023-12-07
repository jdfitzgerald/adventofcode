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

#file = open('day07/real.data','r')
file = open('day07/test.data','r')
buckets = [[],[],[],[],[],[],[]]
for (hand, bid) in [l.strip().split() for l in file]:
    buckets[bucket_hand(hand)].append((hand, bid))

pp.pprint(buckets)
print("-")
rank = "AKQJT98765432"

test = ["T55J5","QQQJA","KK677","KTJJT"]
test = sorted(test,key=lambda x: [rank.rfind(c) for c in x])
print(test)


# problem is subarrays aren't sorting
ranked = [sorted(bucket,key=lambda x: [rank.rfind(c) for c in x]) for bucket in buckets if len(bucket)>0]
ranked = [bucket for bucket in buckets if len(bucket)>0]
pp.pprint(ranked)

score = 0

for (i,(hand,bid)) in enumerate([(hand,bid) for b in ranked for (hand,bid) in b]):
    print(i)
    print(hand,bid)
