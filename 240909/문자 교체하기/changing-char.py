word = input().split()

rep = word[0][0:2]

result = word[1].replace(word[1][0:2], rep)

print(result)