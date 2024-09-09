word = input()
n = int(input())

for i in word[::-1]:
    
    print(i, end="")

    if len(i) > n:
        break