array = []
for i in range(7):
    array.append(list(map(int, input().split())))

array1 = []
for i in range(0, 3):
    array1.append(array[i])

array2 = []
for i in range(4, 7):
    array2.append(array[i])

array3 = [[0] * 3 for _ in range(3)]
for i in range(len(array1)):
    for j in range(len(array1)):
        res = array1[i][j] * array2[i][j]
        array3[i][j] = res

for i in array3:
    print(*i)