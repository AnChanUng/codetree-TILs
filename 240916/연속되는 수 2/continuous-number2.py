n = int(input())

array = []
for _ in range(n):
    number = int(input())
    array.append(number)

cnt = 1
max_cnt = 1
for i in range(len(array)-1):
    if array[i] == array[i+1]:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 1

print(max_cnt)