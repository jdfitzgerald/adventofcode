import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day09/real.data','r')
#file = open('day09/test.data','r')

sum = 0
for line in [l.strip() for l in file]:
    seqs = []
    seqs.append([int(x) for x in line.split()])
    
    s = seqs[0]
    while True:
        next_sequence = []
        for i in range(0, len(s) -1):
            next_sequence.append(s[i+1]-s[i])
        s = next_sequence
        seqs.append(s)
        if s == [0] * len(s):
            break

    for i in range(len(seqs)-2, 0, -1):
        seqs[i-1].insert(0,seqs[i-1][0] - seqs[i][0])

    print(seqs)
    sum += seqs[0][0]

print(sum)