def dfs(x, y):
    dxs = [0, 1]
    dys = [1, 0]

    for i in range(2):
        new_x = x + dxs[i]
        new_y = y + dys[i]

        if 0 <= new_x < n and 0 <= new_y < m:

            if visited[new_x][new_y] == 0 and graph[new_x][new_y] == 1: 
                visited[new_x][new_y] = 1
                dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])