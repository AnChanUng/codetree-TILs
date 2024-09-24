a = list(map(int, input()))

for i in range(len(a)):
    if a[i] == 0:
        a[i] = 1
        break

    if a.count(1) == len(a):
        a[len(a)-1] = 0
        break

res = 0
for i in range(len(a)):
    res += a[i] * 2 ** (len(a)-(i+1))

print(res)