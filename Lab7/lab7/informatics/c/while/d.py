a = int(input())
i = 0
n = 2
ans = "NO"
while n ** i <= a:
    if n **i == a:
        ans = "YES"
    i = i + 1
print(ans)