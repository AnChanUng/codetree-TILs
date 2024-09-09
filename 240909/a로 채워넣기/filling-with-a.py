word = list(input())

word[1] = 'a'
word[-2] = 'a'

result = ''.join(word)
print(result)