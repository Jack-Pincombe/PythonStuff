c = [10,10,20,20,10,30,20]




n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
tot = 0
d = {}
for i in range(n):
    if c[i] in d:
        d.pop(c[i])
        tot += 1
    else:
        d[c[i]] = 1
print tot