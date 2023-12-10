import pprint 
pp = pprint.PrettyPrinter(indent=2)


file = open('day10/real.data','r')
#file = open('day10/test.data','r')

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

path = []
while (i,j) != s_pos:
    path.append((i,j))
    c = matrix[i][j]
    idx2 = entry_shapes[idx].rfind(c)
    d = exits[idx][idx2]
    idx = dirs.index(d)
    (i,j) = (i + d[0], j + d[1])

    
print((1+len(path))//2)