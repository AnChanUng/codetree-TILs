n, m = map(int, input().split())
arr1 = [0] * 1000001
arr2 = [0] * 1000001

time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    
    for _ in range(t):
        arr1[time_a] = arr1[time_a-1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        arr2[time_b] = arr2[time_b-1] + v
        time_b += 1

leader = 0
cnt = 0
for i in range(1, time_a):
    if arr1[i] < arr2[i]:
        if leader != 1:
            cnt += 1
        leader = 1

    elif arr1[i] > arr2[i]:
        if leader != 2:
            cnt += 1
        leader = 2
    
    else:
        if leader != 0:
            cnt += 1
        leader = 0

print(cnt)