n, a = input().split()
n = int(n)

cnt = 0
for i in range(n):
    word = input()
    if a == word:
        cnt += 1

print(cnt)