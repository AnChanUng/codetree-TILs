word = list(input())

a = word[0]
b = word[1]

for i in range(len(word)):
    if word[i] == a:
        word[i] = b
    elif word[i] == b:
        word[i] = a
    else:
        continue

for num in word:
    print(*num, end="")