from itertools import combinations

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

min_num = 100001
for num in combinations(numbers, n-2):
    if sum(num) - s < min_num:
        min_num = min(sum(num)-s, min_num)

print(abs(min_num))