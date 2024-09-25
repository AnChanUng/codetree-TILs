from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
def minus(a, b, c):
    global cnt
    if abs(x-y) <= 2 and abs(b-c) <= 2 and abs(c-a) <= 2:
        cnt += 1

for x, y, z in permutations(numbers, 3):
    minus(x, y, z)

print(n*n*n - cnt)