word = input()

result = word[0:1] + word[2:len(word)-2] + word[-1]

print(result)