offset = 1000


check = [[0] * (2001) for _ in range(2001)]

A = [list(map(int, input().split()))]
B = [list(map(int, input().split()))]
M = [list(map(int, input().split()))]

for rect in A:
    x1, y1, x2, y2 = rect

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            check[x][y] = 1
    
for rect in B:
    x1, y1, x2, y2 = rect

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            check[x][y] = 1
    
for rect in M:
    x1, y1, x2, y2 = rect

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            check[x][y] = 0
    
area = 0
for x in range(0, 2001):
    for y in range(0, 2001):
        if check[x][y] == 1:
            area += 1

print(area)