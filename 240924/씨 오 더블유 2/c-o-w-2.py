n = int(input())
words = list(input())

res = ''
cnt = 0
for i in range(0, len(words)):
    for j in range(i+1, len(words)):
        for k in range(j+1, len(words)):
            res = words[i] + words[j] + words[k]
            if res == 'COW':
                cnt += 1

print(cnt)