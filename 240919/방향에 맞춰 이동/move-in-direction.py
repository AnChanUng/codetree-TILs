n = int(input())
x, y = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)

    if direction == 'W':
        dir = 0
    elif direction == 'E':
        dir = 1
    elif direction == 'N':
        dir = 2
    elif direction == 'S':
        dir = 3

    x += dx[dir] * distance
    y += dy[dir] * distance

print(x, y)