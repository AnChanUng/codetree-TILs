n, m = map(int, input().split())
a = [0] * (1000001)
b = [0] * (1000001)

i = 1
for _ in range(n):
    t, d = input().split()
    t = int(t)
    if d == 'R':
        a[i] = a[i-1] + t
    elif d == 'L':
        a[i] = a[i-1] - t
    i += 1

j = 1
for _ in range(m):
    t, d = input().split()
    t = int(t)
    if d == 'R':
        b[j] = b[j-1] + t
    elif d == 'L':
        b[j] = b[j-1] - t
    j += 1

leader = 0
ans = 1
for num in range(1, i):
    if a[num] >= b[num]:
        if leader == 2:
            ans += 1
        leader = 1
    
    elif a[num] <= b[num]:
        if leader == 1:
            ans += 1
        leader = 2

print(ans)