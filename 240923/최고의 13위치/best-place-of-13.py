n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        if max_cnt < sum(array[i][j:j+3]):
            max_cnt = sum(array[i][j:j+3])
 
print(max_cnt)