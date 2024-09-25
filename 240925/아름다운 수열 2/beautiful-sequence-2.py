from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
check = list(map(int, input().split()))

cnt = 0
for i in range(n-m+1):
    for num in permutations(check, m):
        num = list(num)
        if numbers[i:i+m] == num:
            cnt += 1
            break
    
print(cnt)