a = list(map(int, input().split()))
for i in range(len(a)):
    if i % 2 == 0 and i + 1 < len(a):
        a[i], a[i + 1] = a[i + 1], a[i]
print(' '.join(map(str, a)))
