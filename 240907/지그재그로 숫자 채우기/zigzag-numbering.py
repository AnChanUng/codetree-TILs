n, m = map(int, input().split())

array = [[0] * m for _ in range(n)]

cnt = 0
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            array[j][i] = cnt 
            cnt += 1
    else:
        for j in range(n-1, -1, -1):   
            array[j][i] = cnt
            cnt += 1 

for i in array:
    print(*i)