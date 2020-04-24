a = list(map(int, input().split()))
mn = 99999999999
mx = -mn
ps1 = 0
ps2 = 0
for i in range(len(a)):
    if a[i] < mn:
        mn = a[i]
        ps1 = i
    if a[i] > mx:
        mx = a[i]
        ps2 = i
a[ps1], a[ps2] = a[ps2], a[ps1]
print(' '.join(map(str, a)))
