import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []
for i in range(8):
    array.append(list(map(int, input().split())))

array1 = [[0] * n for _ in range(m)]
for i in range(4):
    for j in range(4):
        array1[i][j] = array[i][j]

array2 = [[0] * n for _ in range(m)] 
for i in range(4, 8):
    for j in range(4):
        array2[i-4][j] = array[i][j]

array3 = [[0] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        if array1[i][j] == array2[i][j]:
            array3[i][j] = 0
        else:
            array3[i][j] = 1

for num in array3:
    print(*num)