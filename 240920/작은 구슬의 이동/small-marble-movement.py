n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(r)

# R U L D
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

array = [[0] * n for _ in range(n)]

mapper = {'R': 0, 'U': 1, 'L': 2, 'D': 3}

move_dir = mapper[d] # 0 출력

for i in range(t):
    nx = r + dx[move_dir]
    ny = c + dy[move_dir]

print(nx, ny)