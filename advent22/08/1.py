import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')

trees = []
for line in [l.strip() for l in file]:
    trees.append([int(x) for x in line])
    

visible = 2*(len(trees) + len(trees[0])) - 4

t_trees = list(map(list,zip(*trees)))
for y in range(1,len(trees)-1):
    for x in range(1,len(trees[0])-1):
        height = trees[y][x]
        print(x,y)
        if (height -1 >= max(trees[y][:x])
        or height -1 >= max(trees[y][x+1:])
        or height -1 >= max(t_trees[x][:y])
        or height -1 >= max(t_trees[x][y+1:])):
            visible += 1

        
pp.pprint(visible)
