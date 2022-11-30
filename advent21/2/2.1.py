import fileinput

filename = './2.1.test'
filename = 'data'

aim=0
depth=0
horizontal=0


for v in fileinput.input(filename):
    (cmd, val) = v.split()
    val = int(val)
    if cmd == 'forward':
        horizontal = horizontal + val
        depth = depth + (aim * val)
    elif cmd == 'down':
        aim = aim + val
    elif cmd == 'up':
        aim = aim - val

print depth * horizontal
