n, m = map(int, input().split())

array = [[0] * m for _ in range(n)]

res = 1
for i in range(n):
    for j in range(m):
        array[i][j] += res
        res += 1

for num in array:
    print(*num)