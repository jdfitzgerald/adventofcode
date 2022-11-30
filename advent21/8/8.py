print(len([n for line in open('data','r') for n in line.strip().split(' | ')[1].split() if len(n) in [2,4,3,7]]))
