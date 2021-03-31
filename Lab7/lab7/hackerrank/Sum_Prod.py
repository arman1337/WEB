import numpy

n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)

s = numpy.sum(a, axis=0)
ans = 1
for i in s:
    ans *= i
print(ans)
