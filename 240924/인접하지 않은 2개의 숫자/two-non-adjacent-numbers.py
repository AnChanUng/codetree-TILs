n = int(input())
numbers = list(map(int, input().split()))

max_res = 0
for i in range(0, len(numbers)):
    res = 0
    for j in range(i+1, len(numbers)):
        if i != (j-1):
            res += numbers[i] + numbers[j]
            max_res = max(max_res, res)
            res = 0

print(max_res)