n, h, t = map(int, input().split())
array = list(map(int, input().split()))

min_res = 10001
for i in range(n-t+1):
    total = 0
    for j in range(t):
        res = abs(h - array[i+j])
        total += res
    
    min_res = min(min_res, total)

print(min_res)