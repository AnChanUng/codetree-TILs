n = int(input())

graph = [[0] * 201 for _ in range(201)]
for _ in range(n):
    x1, y1 = map(int, input().split())

    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            graph[x][y] = 1
            
area = 0
for i in range(201):
    for j in range(201):
        if graph[i][j] == 1:
            area += 1

print(area)