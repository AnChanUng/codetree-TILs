from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
def bfs(x, y):
    global cnt
    if graph[x][y] == 1:
        return 0
    
    queue = deque()
    queue.append((x, y))
    #print("queue", queue)
    visited[x][y] = 0
    cnt += 1
    while queue:
        x, y = queue.popleft()
        #print("x, y", x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 1 and graph[nx][ny] == 0:
                visited[nx][ny] = 0
                #print(visited)
                queue.append((nx, ny))
                cnt += 1
                #print("cnt", cnt)
    return 1

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[1] * n for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    bfs(r-1, c-1)
print(cnt)