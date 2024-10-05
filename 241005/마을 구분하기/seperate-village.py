n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))

for i in answer:
    print(i)