n, k = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = 0
for i in range(len(numbers)-k+1):
    if max_sum < sum(numbers[i:i+k]):
        max_sum = sum(numbers[i:i+k])

print(max_sum)