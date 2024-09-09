words = list(input())

result = ''
for i in range(len(words)):
    if (i+1) % 2 == 0:
        result += words[i]

for word in result[::-1]:
    print(word, end="")