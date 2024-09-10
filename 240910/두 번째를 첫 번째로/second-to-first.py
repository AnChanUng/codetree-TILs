word = list(input())

res1 = word[1] 
res2 = word[0]
for i in range(len(word)):
    if word[i] == res1:
        word[i] = res2

for i in word:
    print(*i, end="")