n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
def solution(x, y):
    global cnt
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[i][j] == 1:
                cnt += 1
    
    return cnt

max_cnt = 0
for i in range(0, n-2):
    for j in range(0, n-2):
     #   print(solution(i, j), end = " ")
        max_cnt = max(max_cnt, solution(i, j))
        cnt = 0
    #print()
print(max_cnt)