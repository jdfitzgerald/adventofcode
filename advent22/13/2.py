import pprint 
import functools

pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')


def cmp(l,r):
    if type(l) == int and type(r) == int:
        if l < r: return 1
        elif l > r: return -1
        else: return 0

    elif type(l) == list and type(r) == int:
        return cmp(l,[r])
    
    elif type(l) == int and type(r) == list:
        return cmp([l],r)

    else:
        for i in range(max(len(l), len(r))):
            if i >= len(l): return 1
            elif i >= len(r): return -1

            result = cmp(l[i],r[i])
            if result != 0: return result
    return 0


packets = [[[2]],[[6]]]
while True:
    try:
        packets.append(eval(file.readline()))
        packets.append(eval(file.readline()))
        file.readline()
    except:
        break

packets.sort(key=functools.cmp_to_key(cmp), reverse=True)
two = packets.index([[2]]) +1 
six = packets.index([[6]]) +1 
print(two*six)



