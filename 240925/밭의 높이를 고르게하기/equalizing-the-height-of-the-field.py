n, h, t = map(int, input().split())
array = list(map(int, input().split()))

min_res = 1001
for i in range(n-t+1):
    res = 0
    for j in range(t):
        res += abs(h - array[j])
        if res < min_res:
            min_res = min(min_res, res)
            res = min_res
    #print("res", res)

print(min_res)