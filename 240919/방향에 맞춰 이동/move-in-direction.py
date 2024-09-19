n = int(input())

ans = [0, 0]
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)

    if direction == 'N':
        ans[1] += distance
            
    elif direction == 'W':
        ans[0] -= distance

    elif direction == 'E':
        ans[0] += distance

    elif direction == 'S':
        ans[1] -= distance

print(*ans)