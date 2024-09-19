n, m = map(int, input().split())
a = [0] * (1000001)
b = [0] * (1000001)

res1 = 0
time = 0
for _ in range(n):
    t, d = input().split()
    t = int(t)

    for _ in range(1, t+1):
        if d == 'L':
            res1 -= 1

        elif d == 'R':
            res1 += 1
        a[time] = res1
        time += 1

res2 = 0
for _ in range(m):
    t, d = input().split()
    t = int(t)

    for _ in range(1, t+1):
        if d == 'L':
            res2 -= 1
        elif d == 'R':
            res2 += 1
        b[time] = res2
        time += 1
cnt = 0
for i in range(1, time):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        cnt += 1

print(cnt)