n, m = map(int, input().split())

array = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
array[x][y] = 1
dir_num = 1
for i in range(2, n*m+1):
    while True:
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]    
    
        if nx < 0 or ny < 0 or nx >= n or ny >= m or array[nx][ny] != 0:
            dir_num = (dir_num + 3) % 4
        else:
            x = nx
            y = ny
            array[x][y] = i

for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print()