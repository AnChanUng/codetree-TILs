n, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * 3 for _ in range(n)]

for i in range(n):
    for j in range(3):
        if 3 <= j+t:
            if (j+t)//3 + i >= n:
                result[i+(j+t)//3 - n][(j+t)%3] = graph[i][j]
            else:
                result[i+(j+t)//3][(j+t)%3] = graph[i][j]
        else:
            result[i][(j+t)%3] = graph[i][j]

for i in range(n):
    for j in range(3):
        print(result[i][j], end= " ")
    print()