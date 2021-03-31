n = int(input())
d = {}
for i in range(n):
    a = [i for i in input().split()]
    d[a[0]] = [float(i) for i in a[1:]]
name = input()
avg = sum(d[name])/len(d[name])
print("%.2f" % avg)
