n, k = map(int, input().split())

array = []
for _ in range(n):
    word = input().split()
    word[0] = int(word[0])
    if word[1] == 'G':
        word[1] = 1
    elif word[1] == 'H':
        word[1] = 2

    array.append(word)

array.sort(key=lambda x: x[0])

max_sum = 0
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if abs(array[i][0] - array[j][0]) <= k:
            result = [x[1] for x in array[i:j+1]]
            if sum(result) > max_sum:
                max_sum = max(max_sum, sum(result))

print(max_sum)