from itertools import combinations

n, s = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

min_num = 10001
for nums in combinations(numbers, len(numbers)-2):
    if sum(nums) - s < min_num:
        min_num = min(min_num, sum(nums))

print(abs(min_num - s))