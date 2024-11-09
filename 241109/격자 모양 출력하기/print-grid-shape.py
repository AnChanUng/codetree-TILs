n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = a * b

for x in graph:
    print(*x)