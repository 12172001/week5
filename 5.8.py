a = list(map(int, input().split()))
mn = 99999999999
mx = -9999999999
for i in range(len(a)):
    if mx <= a[i]:
        mx = a[i]
        n = i
print(mx, n)
