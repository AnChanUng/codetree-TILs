from collections import deque

dx = [+1,-1,+1,-1,-2,-2,+2,+2]
dy = [+2,+2,-2,-2,+1,-1,+1,-1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue: 
        x, y = queue.popleft()    
        
        if x == r2 and y == c2:
            return visited[x][y]-1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

print(bfs(r1, c1))