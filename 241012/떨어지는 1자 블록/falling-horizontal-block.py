n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * len(graph[0]) for _ in range(n)]

for i in range(k-1, k+m-1):
    graph[k][i] = 1

for i in range(len(graph[0])):
    for j in range(n):
        print(graph[i][j], end = " ")
    print()