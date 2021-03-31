def min_(a, b, c, d):
    return min(min(a, b), min(c, d))


a = [int(i) for i in input().split()]
print(min_(a[0], a[1], a[2], a[3]))