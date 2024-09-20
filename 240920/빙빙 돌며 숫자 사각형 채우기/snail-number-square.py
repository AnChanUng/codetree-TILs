n, m = map(int, input().split())

array = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_num = 0
x, y = 0, 0
array[x][y] = 1
for i in range(2, n*m+1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if nx < 0 and nx >= n and ny < 0 and ny >= n or array[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x = x + dx[dir_num]
    y = y + dy[dir_num]
    array[x][y] = i

for i in range(n):
    for j in range(m):
        print(array[i][j], end= " ")
    print()