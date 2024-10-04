import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

min_num = 1000001
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        num = numbers[i] + numbers[j]
        if abs(num) < min_num:
            min_num = min(min_num, num)

print(min_num)