n, t = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
max_cnt = 0
for i in range(n):
    if numbers[i] > t:
        cnt += 1
    else:
        cnt = 0
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)