from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    #print("queue", queue)
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1    
    
    while queue:
        x, y = queue.popleft()
        #print("x, y", x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((x, y))

    return 0

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
        elif graph[i][j] == 2:
            result[i][j] = 0
        elif graph[i][j] == 0:
            result[i][j] = -1

print(result)