array = []
for i in range(2):
    numbers = list(map(int, input().split()))
    print(sum(numbers) / 4, end = " ")
    array.append(numbers)

print()
total = 0
for i in range(4):
    result = 0
    for j in range(2):
        result += array[j][i]
        total += array[j][i]
    print(result/2, end=" ")

print()
print(total / 8)