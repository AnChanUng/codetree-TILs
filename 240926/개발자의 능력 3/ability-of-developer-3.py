import sys
INT_MAX = sys.maxsize

n = 6
arr = list(map(int, input().split()))

def diff(x, y, z):
    sum1 = arr[i] + arr[j] + arr[k]
    sum2 = sum(arr) - sum1
    return abs(sum1 - sum2)

max_sum = INT_MAX 
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            max_sum = min(max_sum, diff(i, j, k)) 

print(max_sum)