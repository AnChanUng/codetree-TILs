n = int(input())
block = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

temp = []
for i in range(n):
    if s1-1 <= i <= e1-1:
        pass
    else:
        temp.append(block[i])

temp2 = []
for i in range(len(temp)):
    if s2-1 <= i <= e2-1:
        pass
    else:
        temp2.append(temp[i])

print(len(temp2))
for num in temp2:
    print(num)