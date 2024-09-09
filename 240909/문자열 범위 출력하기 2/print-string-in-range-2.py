word = input()
n = int(input())

cnt = 0
for i in word[::-1]:
    
    print(i, end="")
    cnt += 1
    if cnt == n:
        break