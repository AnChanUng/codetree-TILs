n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
    
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

res = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny and 0 <= ny < n:
                if array[nx][ny] == 1:
                    cnt += 1

        if cnt >= 3:
            res += 1

print(res)