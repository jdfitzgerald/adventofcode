import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

trees = []
for line in [l.strip() for l in file]:
    trees.append([int(x) for x in line])
    
max_score = 0

for y in range(1,len(trees)-1):
    for x in range(1,len(trees[0])-1):
        height = trees[y][x]
        left = 0
        right = 0
        up = 0
        down = 0

        for i in range(x-1,-1,-1):
            left += 1
            if trees[y][i] >= height: break
        for i in range(x+1,len(trees[y])):
            right += 1
            if trees[y][i] >= height: break
        for i in range(y-1,-1,-1):
            up += 1
            if trees[i][x] >= height: break
        for i in range(y+1,len(trees)):
            down += 1
            if trees[i][x] >= height: break

        score = left*right*up*down
        
        max_score = max(max_score, score)
        if (score == max_score):
            print('y,x,lrud,tot',y,x,left,right,up,down, score)


print(max_score)
