import sys

for i in sys.stdin:
    ab = i.split()
    a = str(a[0])
    b = str(a[1])

if len(a) > len(b):
    res = 'go'
else:
    res = 'no'

print(res)