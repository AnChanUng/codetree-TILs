n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
    
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = 0, 0
cnt = 0
for dx, dy in zip(dxs, dys):
    nx = x + dx
    ny = y + dy
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if array[nx][ny] == 1:
            cnt += 1
            print("array[nx][ny]", array[nx][ny])
            print("cnt", cnt)

print(cnt)