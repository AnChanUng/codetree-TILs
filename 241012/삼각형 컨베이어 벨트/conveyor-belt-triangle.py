import sys
input = sys.stdin.readline

n, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
garo = len(graph)
result = [[0] * garo for _ in range(3)]

for i in range(3):
    for j in range(garo):
        if garo <= j+t:
            if (j+t)//garo + i >= 3:
                result[i+(j+t)//garo-3][(j+t)%garo] = graph[i][j]
            else:
                result[i+(j+t)//garo][(j+t)%garo] = graph[i][j]
        else:
            result[i][(j+t)] = graph[i][j]

for i in range(3):
    for j in range(garo):
        print(result[i][j], end= " ")
    print()