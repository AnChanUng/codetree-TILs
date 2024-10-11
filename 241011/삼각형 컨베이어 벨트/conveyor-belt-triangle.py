n, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * 3 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j + t < len(graph):
            result[i][j] = graph[i][j+t]
        elif j + t > len(graph): 
            result[i][j] = graph[i+1][j+t-len(graph)]
        else:
            result[i][j] = graph[0][j+t-len(graph)]

print(result)