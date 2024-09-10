import sys
input = sys.stdin.readline

word = input()
print(word)

for _ in range(len(word)):
    word = word[-1] + word[0:len(word)-1] 
    print(word)