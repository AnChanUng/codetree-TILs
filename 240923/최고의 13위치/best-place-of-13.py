n = int(input())

array = []
for i in range(n):
    array.append(list(input().split()))

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        if max_cnt < array[i][j:j+3].count('1'):
            max_cnt = array[i][i:j+3].count('1')
 
print(max_cnt)