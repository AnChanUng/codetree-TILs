# 변수 선언 및 입력
n, m = map(int, input().split())
height = [list(map(int, input().split())) for _ in range(n)]

fertilizer = [[False] * n for _ in range(n)]
# 초기 특수 영양제 위치 설정
for i in range(n - 2, n):
    for j in range(2):
        fertilizer[i][j] = True

# 문제에서 주어진 방향 순서대로 → ↗ ↑ ↖ ← ↙ ↓ ↘
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

# 이동 후 위치 계산 함수
def next_pos(x, y, d, p):
    return (x + dxs[d] * p + n * p) % n, (y + dys[d] * p + n * p) % n

# 시뮬레이션 함수
def simulate(d, p):
    # Step 1: 특수 영양제 이동
    next_fert = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if fertilizer[i][j]:
                nx, ny = next_pos(i, j, d, p)
                next_fert[nx][ny] = True
    
    # Step 2: 이동한 위치에서 성장
    for i in range(n):
        for j in range(n):
            if next_fert[i][j]:
                height[i][j] += 1
    
    # Step 3: 대각선 방향 추가 성장
    for i in range(n):
        for j in range(n):
            if next_fert[i][j]:
                cnt = sum(1 for dx, dy in zip(dxs[1::2], dys[1::2]) 
                          if 0 <= i + dx < n and 0 <= j + dy < n and height[i + dx][j + dy] >= 1)
                height[i][j] += cnt
    
    # Step 4: 새로운 영양제 추가 및 기존 영양제 제거
    for i in range(n):
        for j in range(n):
            if next_fert[i][j]:
                fertilizer[i][j] = False
            elif height[i][j] >= 2:
                fertilizer[i][j] = True
                height[i][j] -= 2

# m번 시뮬레이션 실행
for _ in range(m):
    d, p = map(int, input().split())
    simulate(d - 1, p)

# 결과 출력
print(sum(sum(row) for row in height))