import pprint
pp = pprint.PrettyPrinter(indent=2)

def bucket_hand(hand) -> int:
    # special case cause I'm lazy
    if hand == 'JJJJJ':
        return 6

    cards = [(x, hand.count(x)) for x in set(hand)]
    cards.sort(key=lambda x: x[1], reverse=True)
    
    jokers = [(card, x) for (card, x) in cards if card=='J']
    if len(jokers):
        jokers=jokers[0]
        cards.remove(jokers)
        (card, c) = cards[0]
        cards[0] = (card, c+jokers[1])

    if cards[0][1] == 5:
        return 6
    elif cards[0][1] == 4:
        return 5
    elif cards[0][1] == 3 and cards[1][1] == 2:
        return 4
    elif cards[0][1] == 3:
        return 3
    elif cards[0][1] == 2 and cards[1][1] == 2:
        return 2
    elif cards[0][1] == 2:
        return 1
    return 0

file = open('day07/real.data','r')
#file = open('day07/test.data','r')
buckets = [[],[],[],[],[],[],[]]
for (hand, bid) in [l.strip().split() for l in file]:
    buckets[bucket_hand(hand)].append((hand, int(bid)))

rank = "AKQT98765432J"[::-1]


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
# 252898370