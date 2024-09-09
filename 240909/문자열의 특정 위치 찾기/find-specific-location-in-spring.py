words = input().split()

if words[1] in words[0]:
    print(words[0].index(words[1]))
else:
    print("No")