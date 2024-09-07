array = []
for i in range(2):
    numbers = list(map(int, input().split()))
    garo = round((sum(numbers)/4), 1)
    print(garo, end = " ")
    array.append(numbers)

print()
total = 0
for i in range(4):
    result = 0
    for j in range(2):
        result += array[j][i]
        total += array[j][i]
    sero = round(result/2, 1)
    print(sero, end=" ")

print()
res = round(total / 8, 1)
print(res)