from collections import deque

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global k
    queue = deque()
    queue.append((x, y))    
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (r2 - 1, c2 - 1):
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                    elif graph[nx][ny] == 1 and k > 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                        k -= 1                
    return -1

# 입력 처리
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

# BFS 실행 및 결과 출력
print(bfs(r1 - 1, c1 - 1))