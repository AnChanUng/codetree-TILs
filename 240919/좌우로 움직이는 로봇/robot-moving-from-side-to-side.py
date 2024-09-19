n, m = map(int, input().split())
a = [0] * (1000001)
b = [0] * (1000001)

time_a = 1
for _ in range(n):
    t, d = input().split()
    t = int(t)

    for _ in range(1, t+1):
        if d == 'L':
            a[time_a] = a[time_a-1] - 1
        elif d == 'R':
            a[time_a] = a[time_a-1] + 1
        time_a += 1

time_b = 1
for _ in range(m):
    t, d = input().split()
    t = int(t)

    for _ in range(1, t+1):
        if d == 'L':
            b[time_b] = b[time_b-1] - 1
        elif d == 'R':
            b[time_b] = b[time_b-1] + 1
        time_b += 1

if time_a < time_b:
    for i in range(time_a, time_b):
        a[i] = a[i-1]
elif time_a > time_b:
    for i in range(time_b, time_a):
        b[i] = b[i-1]

cnt = 0
time_max = max(time_a, time_b)
for i in range(1, time_max):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        cnt += 1

print(cnt)