n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def dfs(x, y):
    dxs = [0, 1]
    dys = [1, 0]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if 0 <= new_x < n and 0 <= new_y < m:
            if visited[nx][y] == 0 and graph[nx][ny] == 1: 
                visited[nx][ny] = 1
                dfs(nx, ny)

visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])