n = int(input())
numbers = list(map(int, input().split()))

max_res = 0
for i in range(0, len(numbers)):
    res = 0
    for j in range(i+2, len(numbers)):
        if max_res < numbers[i] + numbers[j]:
            res = numbers[i] + numbers[j]
            max_res = max(max_res, res)

print(max_res)