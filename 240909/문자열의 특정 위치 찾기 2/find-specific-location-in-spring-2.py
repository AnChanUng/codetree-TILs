word = input()

words = ["apple", "banana", "grape", "blueberry", "orange"]

cnt = 0
for i in range(len(words)):
    if words[i][2] == word or words[i][3] == word:
        cnt += 1
        print(words[i])

print(cnt)