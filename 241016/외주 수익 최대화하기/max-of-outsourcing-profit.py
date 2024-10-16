n = int(input())
graph = []
for i in range(n):
    n, p = map(int, input().split())
    graph.append([n, p])

sum_t = 0
max_t = 0
max_n = 0
for i in range(len(graph)):
    if max_n <= n:
        max_n += graph[i][0]
        sum_t += graph[i][1]
    max_t = max(max_t, sum_t)

print(max_t)