import pprint
pp = pprint.PrettyPrinter(indent=2)



grid = []
file = open('day14/real.data','r')
#file = open('day14/test.data','r')
for line in [l.strip() for l in file]:
    grid.append(list(line))


# column-wise iteration
def roll_north(grid):
    for j in range(len(grid[0])):
        queue = []
        for i in range(len(grid)):
            if grid[i][j] == '#':
                queue = []
            elif grid[i][j] == 'O' and queue != []:
                (ti, tj) = queue.pop()
                grid[ti][tj] = 'O'
                grid[i][j] = '.'
                queue.insert(0,(i,j)) # current slot is now empty
            elif grid[i][j] == '.':
                queue.insert(0,(i,j)) # slot is empty
    return grid


grid = roll_north(grid)

# score
total = 0
for r in range(len(grid)):
    multiplier = len(grid) - r
    score = grid[r].count('O') * multiplier
    total += score

print(total)
