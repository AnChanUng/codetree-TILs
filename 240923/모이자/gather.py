n = int(input())
numbers = list(map(int, input().split()))

array = []
for num in range(n):
    result = 0
    for i in range(n):
        dis = abs(num - i)
        result += numbers[i] * dis
    array.append(result)

print(min(array))