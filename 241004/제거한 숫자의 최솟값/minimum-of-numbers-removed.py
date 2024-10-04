import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
array = sorted(map(int, input().split()))

min_m = 0

for i in range(n // 2):
    pair_sum = array[i] + array[n - 1 - i]
    min_m = max(min_m, pair_sum)

if n % 2 == 1:
    middle_value = array[n // 2]
    min_m = max(min_m, middle_value)

print(min_m)