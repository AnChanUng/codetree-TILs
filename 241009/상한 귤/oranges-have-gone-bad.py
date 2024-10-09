from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    distance = [[0] * n for _ in range(n)]
    
    while queue:
        x, y = queue.popleft()
        
        if graph[x][y] == 2:
            return distance[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    return -1

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result[i][j] = bfs(i, j)
        elif graph[i][j] == 2:
            result[i][j] = 0

for i in range(n):
    for j in range(n):
        print(result[i][j], end = " ")
    print()