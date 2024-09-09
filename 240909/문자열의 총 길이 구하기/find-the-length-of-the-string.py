words = input().split()

cnt = 0
for word in words:
    cnt += len(word)

print(cnt)