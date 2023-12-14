import pprint
pp = pprint.PrettyPrinter(indent=2)



grid = []
#file = open('day14/real.data','r')
file = open('day14/test.data','r')
for line in [l.strip() for l in file]:
    grid.append(list(line))


# column-wise iteration
def roll(grid, direction):
    # define the two ranges based on the direction and it should be easy to iterate through
    # double check order of lists - think it aint right
    if direction == 'north':
        outer = range(len(grid[0]))
        inner = range(len(grid))
    elif direction == 'south':
        outer = range(len(grid[0]))
        inner = reversed(range(len(grid)))
    elif direction == 'west':
        outer = range(len(grid))
        inner = range(len(grid[0]))
    else:
        outer = range(len(grid))
        inner = reversed(range(len(grid[0])))
    # etc

    for i in outer:
        queue = []
        for j in inner:
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


for i in range(1):
    grid = roll(grid, 'north')
    grid = roll(grid, 'west')
    grid = roll(grid, 'south')
    grid = roll(grid, 'east')

for r in grid:
    pp.pprint("".join(r))

# score
total = 0
for r in range(len(grid)):
    multiplier = len(grid) - r
    score = grid[r].count('O') * multiplier
    total += score

print(total)
