import pprint
import copy
pp = pprint.PrettyPrinter(indent=2)


def score_grid(grid):
    total = 0
    for r in range(len(grid)):
        multiplier = len(grid) - r
        score = grid[r].count('O') * multiplier
        total += score
    return total
def print_grid(grid):
    for r in grid:
        pp.pprint("".join(r))
    print('============')


# column-wise iteration
def roll(grid, direction):
    # define the two ranges based on the direction and it should be easy to iterate through
    # double check order of lists - think it aint right
    width = len(grid[0])
    height = len(grid)

    if direction in ('north', 'south'):
        outer = range(width)
        inner = range(height)
    else:
        outer = range(height)
        inner = range(width)

    def get_pos(i,j, direction):
       if direction == 'north':
           return (j,i)
       elif direction == 'south':
           return (height-j-1,i)
       elif direction == 'west':
           return (i,j)
       else:
           return (i,width-j-1)


    for y in outer:
        queue = []
        for x in inner:
            (i,j) = get_pos(y,x,direction)
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

grid = []
#file = open('day14/real.data','r')
file = open('day14/test.data','r')
for line in [l.strip() for l in file]:
    grid.append(list(line))


for i in range(1000000000):
    grid = roll(grid, 'north')
    grid = roll(grid, 'west')
    grid = roll(grid, 'south')
    grid = roll(grid, 'east')

    if grid == grid1: 
        break
    if (i%100000) == 0:
        print(i)

print_grid(grid)
print(score_grid(grid))