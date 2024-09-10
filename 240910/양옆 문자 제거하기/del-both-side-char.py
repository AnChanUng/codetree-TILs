word = input()

result = word[0:2] + word[3:len(word)-2] + word[-1]

print(result)