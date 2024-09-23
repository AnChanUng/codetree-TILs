n, m = map(int, input().split())

array = [list(input().split()) for _ in range(n)]

cnt = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i+1, n-1):
            for l in range(j+1, m-1):
                if array[0][0] != array[i][j] and array[i][j] != array[k][l] and array[k][l] != array[n-1][m-1]:
                    cnt += 1

print(cnt)