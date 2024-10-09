from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))    
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        if graph[r2-1][c2-1] == 0:
            return visited[r2-1][c2-1]

        if k <= -1
            return -1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny] == 1):
                graph[nx][ny] = 1
                visited[nx][ny] = visited[nx][ny] + 1
                queue.append((nx, ny))
    return -1

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

print(bfs(r1-1, c1-1))