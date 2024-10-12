import sys
input = sys.stdin.readline

n, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
garo = len(graph[0])
result = [[0] * garo for _ in range(3)]

for i in range(3):
    for j in range(garo):
        new_row = (i + (j + t) // garo) % 3
        new_col = (j + t) % garo
        result[new_row][new_col] = graph[i][j]

for i in range(3):
    for j in range(garo):
        print(result[i][j], end= " ")
    print()