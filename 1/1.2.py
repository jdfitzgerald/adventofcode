import fileinput

ln=0

sl0 = 0
sl1 = 0
sl2 = 0

c = 0
tot = 0
for v in fileinput.input():
    v = int(v)
    if c >= 3:
        if sl2 < sl1 + v:
            tot = tot + 1

    sl2 = sl1 + v
    sl1 = sl0 + v
    sl0 = v
    c = c + 1
    print c, v, sl2, sl1, sl0, tot

print tot
