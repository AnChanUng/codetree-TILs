from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
check = list(map(int, input().split()))

cnt = 0
for i in range(n-m+1):
    if Counter(numbers[i:i+m]) == Counter(check):
        cnt += 1
    
print(cnt)