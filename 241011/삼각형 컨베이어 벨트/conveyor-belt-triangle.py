n, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * 3 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j + t <  
            result[i][j] = graph[i][j+t]

print(result)