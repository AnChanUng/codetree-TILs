import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
array = sorted(map(int, input().split()))

min_m = 


for i in range((n + 1) // 2):
    if i < n // 2:
        pair_sum = array[i] + array[n - 1 - i]
        min_m = max(min_m, pair_sum)

if n % 2 == 1:
    min_m = max(min_m, array[n // 2])

print(min_m)