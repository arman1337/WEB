def xor(x, y):
    if x + y == 0 or x + y == 2:
        return 0
    else:
        return 1


a, b = [int(i) for i in input().split()]
print(xor(a, b))
