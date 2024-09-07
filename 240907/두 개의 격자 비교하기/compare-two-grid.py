import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array1 = []
for i in range(n):
    array1.append(list(map(int, input().split())))

array2 = []
for j in range(n):
    array2.append(list(map(int, input().split())))

array3 = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if array1[i][j] == array2[i][j]:
            array3[i][j] = 0
        else:
            array3[i][j] = 1

for num in array3:
    print(*num)