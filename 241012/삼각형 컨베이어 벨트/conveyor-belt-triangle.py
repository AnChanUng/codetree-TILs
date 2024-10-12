n, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
garo = len(graph)
result = [[0] * garo for _ in range(n)]
print("result", result)
for i in range(n):
    for j in range(garo):
        if garo <= j+t:
            if (j+t)//garo + i >= n:
                result[i+(j+t)//garo - n][(j+t)%garo] = graph[i][j]
            else:
                result[i+(j+t)//garo][(j+t)%garo] = graph[i][j]
        else:
            result[i][(j+t)%garo] = graph[i][j]

for i in range(n):
    for j in range(garo):
        print(result[i][j], end= " ")
    print()