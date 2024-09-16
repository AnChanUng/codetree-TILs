n = int(input())
array = [int(input()) for _ in range(n)]

cnt = 1
max_cnt = 0
for i in range(n):
    if i >= 1 and array[i] > 0 and array[i-1] > 0:
        cnt += 1
    elif i >= 1 and array[i] < 0 and array[i-1] < 0:
        cnt += 1
    else:
        cnt = 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)