from itertools import MAX_INF

n = int(input())
numbers = list(map(int, input().split()))

max_num = MAX_INF
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] < max_num:
            max_num = min(max_num, numbers[i]+numbers[j])

print(max_num)