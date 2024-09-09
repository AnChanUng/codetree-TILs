word = list(input())

a = word[0]
b = word[1]

word[0] = b
word[1] = a

for ww in word:
    print(ww, end="")