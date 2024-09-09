a = list(input())

cnt = 1
result = ''
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        cnt += 1
    else:
        result += a[i] + str(cnt)
        cnt = 1

result += a[-1] + str(cnt)
print(len(result))
print(result)