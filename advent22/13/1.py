import pprint 
pp = pprint.PrettyPrinter(indent=2)

#file = open('test','r')
file = open('data','r')


def cmp(l,r):
    if type(l) == int and type(r) == int:
        if l < r: return True
        elif l > r: return False
        else: return None

    elif type(l) == list and type(r) == int:
        result = cmp(l,[r])
        if result is not None:
            return result
    
    elif type(l) == int and type(r) == list:
        result = cmp([l],r)
        if result is not None:
            return result

    else:
        for i in range(max(len(l), len(r))):
            if i >= len(l): return True
            elif i >= len(r): return False

            result = cmp(l[i],r[i])
            if result is not None:
                return result




index = 0
trues = []
while True:
    try:
        left = eval(file.readline())
        right = eval(file.readline())
        gap = file.readline()
    except:
        break

    index += 1
    print(left)
    print(right)
    result = cmp(left,right)
    if result is True: 
        trues.append(index)

print(trues)
print(sum(trues))
