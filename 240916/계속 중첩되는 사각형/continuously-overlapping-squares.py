n = int(input())

graph = [[0] * 201 for _ in range(201)]
area = 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split()) 

for x in range(x3, x4+1):
    for y in range(y3, y4+1):
        if graph[x][y]:
            graph[x][y] = 2
        else:
            graph[x][y] = 1
    
for i in range(201):
    for j in range(201):
        if graph[i][j] == 1 or graph[i][j] == 2:
            area += 1  
    
print(area)