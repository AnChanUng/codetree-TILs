import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
check = list(map(int, input().split()))

cnt = 0
for i in range(n-m+1):
    if sorted(numbers[i:i+m]) == sorted(check):
        cnt += 1
    
print(cnt)