from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    while queue:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    
    return cnt

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited [[0] for _ in range(n) for _ in range(m)]

array = []      
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            array.append(bfs(i, j))

for i in array:
    print(i)