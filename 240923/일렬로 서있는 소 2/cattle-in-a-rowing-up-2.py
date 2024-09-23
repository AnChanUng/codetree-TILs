n = int(input())
numbers = list(map(int, input().split()))

cnt = 0 
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i] <= numbers[j] <= numbers[k]:
                cnt += 1
print(cnt)