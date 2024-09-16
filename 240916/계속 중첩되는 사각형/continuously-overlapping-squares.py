n = int(input())
rect = [list(map(int, input().split())) for _ in range(n)]

graph = [[0] * 201 for _ in range(201)]
area = 0

for i in range(n):
    x1, y1, x2, y2 = rect[i]

    if i % 2 == 1:
        color = 2
    else:
        color = 1
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = color

for x in range(201):
    for y in range(201):
        if graph[x][y] == 2:
            area += 1

print(area)