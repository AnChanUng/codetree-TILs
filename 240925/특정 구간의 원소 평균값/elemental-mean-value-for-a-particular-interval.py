n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        res = sum(numbers[i:j+1]) / len(numbers[i:j+1]) # 평균
        if res in numbers[i:j+1]:
            cnt += 1

print(cnt)