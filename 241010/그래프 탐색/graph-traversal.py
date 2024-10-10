n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0 
def dfs(vertex):
    global cnt
    for i in graph[vertex]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            dfs(i)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)   

visited[1] = 1
dfs(1)

print(cnt)