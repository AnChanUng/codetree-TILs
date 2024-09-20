n, m = map(int, input().split())
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

array = [[0] * (m) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
array[x][y] = words[0]

dir_num = 0
for i in range(1, n*m+1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    
    if 0 <= x < nx and 0 <= y < ny and array[nx][ny] == 0:
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        array[x][y] = words[i % 26]
    else:
        dir_num = (dir_num + 1) % 4
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        array[x][y] = words[i % 26]

for i in range(n):
    for j in range(m):
        print(array[i][j], end = " ")
    print()