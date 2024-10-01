n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
def dfs(x, y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if graph[nx][ny] == 1:
            cnt += 1

dfs(0, 0)

print(array)