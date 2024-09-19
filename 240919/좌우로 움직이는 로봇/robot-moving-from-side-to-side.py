n, m = map(int, input().split())
a = [0] * (1000001)
b = [0] * (1000001)

res1 = 0
time_a = 0
for _ in range(n):
    t, d = input().split()
    t = int(t)

    for _ in range(1, t+1):
        if d == 'L':
            res1 -= 1

        elif d == 'R':
            res1 += 1
        a[time_a] = res1
        time_a += 1

res2 = 0
time_b = 0
for _ in range(m):
    t, d = input().split()
    t = int(t)

    for _ in range(1, t+1):
        if d == 'L':
            res2 -= 1
        elif d == 'R':
            res2 += 1
        b[time_b] = res2
        time_b += 1

cnt = 0
for i in range(1, time_a+1):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        cnt += 1

print(cnt)