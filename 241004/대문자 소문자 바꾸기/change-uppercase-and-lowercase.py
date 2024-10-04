word = list(input())

for i in range(len(word)):
    if 65 <= ord(word[i]) <= 96:
        word[i] = word[i].lower()
    else:
        word[i] = word[i].upper()

for i in word:
    print(i, end="")