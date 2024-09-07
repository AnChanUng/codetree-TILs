n, m = map(int, input().split())

array = [[0] * m for _ in range(n)]

cnt = 0
for i in range(m):
    for j in range(n):
        array[j][i] = cnt
        cnt += 1

for num in array:
    print(*num)