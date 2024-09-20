n = int(input())

array = [[0] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dir_num = 0
x = n - 1
y = n - 1
array[x][y] = n * n
for i in range(2, n*n+1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 0:
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        array[x][y] = i

    else:
        dir_num = (dir_num+1) % 4
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        array[x][y] = i

for i in range(n):
    for j in range(n):
        print(array[i][j], end = " ")
    print()