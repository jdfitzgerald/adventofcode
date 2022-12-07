import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
#file = open('data','r')

d_stack = ['']
d_sizes = {}

def run_cmd(cmd):
    global d_stack
    if cmd != '$ ls': 
        if cmd == '$ cd /': d_stack = ['']
        elif cmd == '$ cd ..': d_stack.pop()
        else:
            d = line[5:]
            d_stack.append(d)


for line in [l.strip() for l in file]:
    if line[0] == '$':
        run_cmd(line)
    else:
        if line[:3] == 'dir': continue

        for i in range(len(d_stack), 0, -1):
            cur_d = '/'.join(d_stack[:i])
            if cur_d not in d_sizes: d_sizes[cur_d] = 0
            d_sizes[cur_d] += int(line.split(' ')[0])

d_space = 70000000 - d_sizes['']
d_needed = d_space - 30000000


d_sum = 0
for d in d_sizes:
    print(d, d_sizes[d])
    if d_sizes[d] <= 100000:
        d_sum+=d_sizes[d]

print(d_sum)
