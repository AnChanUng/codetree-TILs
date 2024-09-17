n, m = map(int, input().split())

pos_a = [0] * (1000000 + 1)
pos_b = [0] * (1000000 + 1)

time_a = 1
for _ in range(n):
    d, t = input().split()
    t = int(t)
    
    for _ in range(t):
        if d == 'R':
            pos_a[time_a] = pos_a[time_a - 1] + 1
        else:  
            pos_a[time_a] = pos_a[time_a - 1] - 1
        time_a += 1

time_b = 1
for _ in range(m):
    d, t = input().split()
    t = int(t)
    
    for _ in range(t):
        if d == 'R':
            pos_b[time_b] = pos_b[time_b - 1] + 1
        else:  
            pos_b[time_b] = pos_b[time_b - 1] - 1
        time_b += 1

ans = -1

for i in range(1, time_a):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)