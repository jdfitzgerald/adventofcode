import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day13/real.data','r')
#file = open('day13/test.data','r')

patterns = []
pattern = []
for line in [l.strip() for l in file]:
    if line == '':
        patterns.append(pattern)
        pattern = []
        continue
    pattern.append(list(line))

patterns.append(pattern)

total_score = 0
for p in patterns:
    score = 0
    # horizontal check
    for i in range(0,len(p)-1):
        tail = p[i+1:2*i+2]
        head = p[:i+1][::-1][:len(tail)]

        diff_count=0
        for x in range(0, len(tail)):
            if tail[x] != head[x]:
                diffs = [1 for y in range(len(tail[x])) if tail[x][y] != head[x][y]]
                diff_count += len(diffs)
                if diff_count > 1:
                    break

        if diff_count == 1:
            score = 100 * (i+1)
            break
        
    if score == 0:
        # vertical check
        p = [[r[i] for r in p] for i in range(len(p[0]))]
        for i in range(0,len(p)-1):
            tail = p[i+1:2*i+2]
            head = p[:i+1][::-1][:len(tail)]

            diff_count=0
            for x in range(0, len(tail)):
                if tail[x] != head[x]:
                    diffs = [1 for y in range(len(tail[x])) if tail[x][y] != head[x][y]]
                    diff_count += len(diffs)
                    if diff_count > 1:
                        break

            if diff_count == 1:
                score = (i+1)
                break
    
    total_score += score
print(total_score)