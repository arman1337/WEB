import numpy

n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)

mean = numpy.mean(a, axis=1)
var = numpy.var(a, axis=0)
std = numpy.std(a, axis=None)

print(mean)
print(var)
print(std)