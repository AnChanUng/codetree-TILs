a = list(map(int, input()))

for i in range(len(a)):
    if a[i] == 0:
        a[i] = 1
        break

res = 0
for i in range(len(a)):
    res += a[i] * 2 ** (len(a)-(i+1))

print(res)