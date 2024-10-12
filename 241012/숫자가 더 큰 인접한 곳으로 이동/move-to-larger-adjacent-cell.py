from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    result.append(graph[x][y])

    while queue:
        x, y = queue.popleft()
        standard = graph[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph) and not visited[nx][ny] and standard < graph[nx][ny]:
                visited[nx][ny] = 1
                result.append(graph[nx][ny])
                queue.append((nx, ny))
                break   

n, r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * len(graph[0]) for _ in range(len(graph))]
result = []

bfs(r-1, c-1)
print(*result)