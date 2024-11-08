word = lits(input())

print(len(word))

for i in range(len(word)):
    if i % 2 == 0:
        print(word[i])