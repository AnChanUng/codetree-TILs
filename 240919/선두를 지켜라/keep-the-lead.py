n, m = map(int, input().split())
a = [0] * (1000001)
b = [0] * (1000001)

time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a[time_a] = a[time_a-1] + v
        time_a += 1

time_b = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        b[time_a] = b[time_a-1] + v
        time_b += 1

leader = 0
ans = 0
for i in range(1, time_a):
    if a[i] > b[i]:
        if leader == 2:
            ans += 1
        leader = 1
    
    elif a[i] < b[i]:
        if leader == 1:
            ans += 1
        leader = 2

print(ans)