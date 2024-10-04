n = int(input())
numbers = list(map(int, input().split()))

min_num = 1001
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        num = abs(numbers[i] + numbers[j])
        if num < max_num:
            min_num = min(min_num, num)

print(max_num)