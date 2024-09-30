n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# def can_go(x, y):
#     if not in_range(x, y):
#         return False
    
#     if visited[x][y] or graph[x][y] == 0:
#         return False
    
#     return True

def dfs(x, y):
    dxs = [0, 1]
    dys = [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < n and 0 <= new_y < m:

            if visited[new_x][new_y] == 0 and graph[new_x][new_y] == 1: 
                visited[new_x][new_y] = 1
                dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])