import pprint 
import os

pp = pprint.PrettyPrinter(indent=2)

#filename = os.path.dirname(__file__)+'/test'
filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')

jet_str = file.readline().strip()

rock_shapes = [
    [[1,1,1,1]],
    [[0,1,0],[1,1,1],[0,1,0]],
    [[1,1,1],[0,0,1],[0,0,1]],
    [[1],[1],[1],[1]],
    [[1,1],[1,1]],
]

def print_chamber():
    for y in range(len(chamber)-2,-1,-1):
        s = ''.join(['.' if i == 0 else '#' for i in chamber[y] ])
        print("|%s|"%s)
    
    print('+-------+')

def rock_shape_gen():
    i = 0
    while True:
        yield rock_shapes[i]
        i = (i + 1) % len(rock_shapes)

def jet_gen():
    i = 0
    while True:
        yield 1 if jet_str[i] == '>' else -1
        i = (i + 1) % len(jet_str)

max_height = 0
width = 7
spawn_height = 3
num_rocks = 2022
#num_rocks = 10

shapes = rock_shape_gen()
jets = jet_gen()


chamber = {
    -1:[1 for i in range(width)],
    0:[0 for i in range(width)],
    }

def fill_chamber(height):
    for i in range(max_height, height):
        if i not in chamber:
            chamber[i] = [0 for i in range(width)]
def test_move(left,height,shape):
    if left < 0 or left+len(shape[0]) > len(chamber[0]):
        return False
    for y in range(len(shape)):
        if (y+height) in chamber:
            for x in range(len(shape[0])):
                if shape[y][x] + chamber[y+height][x+left] > 1:
                    return False
    return True


for rock_num in range(num_rocks):
    height = max_height + spawn_height
    fill_chamber(height+4)

    left = 2
    shape = next(shapes)

    for n in range(height+1):
        jet = next(jets)
        if test_move(left+jet, height, shape):
            left += jet
        if not test_move(left, height-1, shape):
            for y in range(len(shape)):
                for x in range(len(shape[0])):
                    chamber[height+y][x+left] += shape[y][x]


            max_height = max(max_height, height+y+1)
            break
        height -= 1

print("max height", max_height)
#print_chamber()