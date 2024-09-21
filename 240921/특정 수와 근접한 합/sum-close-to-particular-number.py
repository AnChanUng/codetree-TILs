from itertools import combinations

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

min_diff = 100001

for combo in combinations(numbers, 2):
    sum_excluded = sum(combo)
    
    remaining_sum = sum(numbers) - sum_excluded
    
    diff = abs(remaining_sum - s)
    
    if diff < min_diff:
        min_diff = diff

print(min_diff)