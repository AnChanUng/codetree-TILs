n, m = map(int, input().split())
a = [0] * (1000000+1)
b = [0] * (1000000+1)

time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a[time_a] = a[time_a-1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b[time_b] = b[time_b-1] + v
        time_b += 1

cnt = 0
for i in range(len(a)):
    if a[i] > b[i]:
        cnt += 1

print(cnt)