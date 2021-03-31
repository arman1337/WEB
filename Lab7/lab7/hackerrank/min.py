import numpy

n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)

s = numpy.min(a, axis=1)

print(max(s))