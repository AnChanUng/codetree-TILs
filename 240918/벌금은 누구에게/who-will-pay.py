import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

array = [int(input()) for _ in range(m)]
arr = [0] * (n+1)

ans = -1
for num in array:
    arr[num] += 1
    
    if arr[num] >= k:
        ans = num
        break

print(ans)