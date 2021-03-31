a = int(input())
b = int(input())
b = int(b**(1/2)+1)

for i in range(a, b):
    if i != 0 or i != 1 or i != -1:
        print(i**2, end=" ")