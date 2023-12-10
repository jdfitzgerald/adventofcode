import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day10/real.data','r')
#file = open('day10/test2.data','r') # result should be 10

matrix = []
s_pos = (-1,-1)
for (i,line) in enumerate([l.strip() for l in file]):
    j = line.rfind('S')
    if (j>-1):
        s_pos = (i,j)
    matrix.append(line)

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
entry_shapes = [
    '7F|',
    'JL|',
    'LF-',
    'J7-'
    ]
exits = [[(0,-1),(0,1),(-1,0)],
         [(0,-1),(0,1),(1,0)],
         [(-1,0),(1,0),(0,-1)],
         [(-1,0),(1,0),(0,1)]]

width = len(matrix[0])
height = len(matrix)

for (idx,d) in enumerate(dirs):
    (i,j) = (s_pos[0] + d[0], s_pos[1] + d[1])
    if 0 <= j < width and 0 <= i < height:
        c = matrix[i][j]
        if c in entry_shapes[idx]:
            break

# i,j contain the first found valid route, d is the offset and idx is the index of the offset
print('starting at ',s_pos, ' going to ', (i,j), d,idx)

loop = [s_pos]
while (i,j) != s_pos:
    loop.append((i,j))
    c = matrix[i][j]
    idx2 = entry_shapes[idx].rfind(c)
    d = exits[idx][idx2]
    idx = dirs.index(d)
    (i,j) = (i + d[0], j + d[1])

    

# for each point that's not in the loop start at it and count the number of
# times it crosses the loop. If the count is even then it's outside the loop
# https://en.wikipedia.org/wiki/Point_in_polygon
# scan left to right and see how often we cross
# xF-J <- one cross
# xF-7 <- two crosses

skip = '-'
in_loop = 0
for i in range(0,height):
    for j in range(0,width):
        if (i,j) not in loop:
            # shoot beam
            journey = ''
            for b in range(j+1, width):
                if (i,b) in loop and matrix[i][b] not in skip:
                    journey += matrix[i][b]
                    
            journey = journey.replace('L7', 'x')
            journey = journey.replace('FJ', 'x')
            if len(journey) % 2:
                in_loop += 1
                    
print(in_loop)