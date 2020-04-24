a = list(map(int, input().split()))
mn = 999999999999999999
for i in range(len(a)):
    if a[i] > 0:
        if mn > a[i]:
            mn = a[i]
print(mn)
