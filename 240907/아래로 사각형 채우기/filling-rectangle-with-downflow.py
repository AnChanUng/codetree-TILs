n = int(input())

array = [[0] * n for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        array[j][i] = cnt
        cnt += 1

for num in array:
    print(*num)