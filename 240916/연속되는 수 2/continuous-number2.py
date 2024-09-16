n = int(input())

array = []
for _ in range(n):
    number = int(input())
    array.append(number)

ans, cnt = 0, 0
for i in range(n):
    if i >= 1 and array[i] == array[i-1]:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)