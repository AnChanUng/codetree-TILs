array = []
for _ in range(4):
    array.append(list(map(int, input().split())))

res = 0
for i in range(0, 4):
    for j in range(0, i+1):
        res += array[i][j]

print(res)