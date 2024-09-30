n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def dfs(x, y):
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < n and 0 <= new_y < m
            if visited[new_x][new_y] == 0 and graph[new_x][new_y] == 1: 
                visited[new_x][new_y] = 1
                dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])