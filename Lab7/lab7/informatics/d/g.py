a = [int(i) for i in input().split()]

max_n = -1
max_i = -1

for i in range(len(a)):
    if a[i] > max_n:
        max_n = a[i]
        max_i = i
print(max_n, max_i)