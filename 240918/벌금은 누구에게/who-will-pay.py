n, m, k = map(int, input().split())

arr = [0] * (m+1)
array = []
for _ in range(m):
    array.append(int(input()))

cnt = 0
for i in array:

    if arr[i] != k:
        arr[i] += 1
        print(arr.index(arr[i]))
        break
    else:
        arr[i] += 1
        if arr[i] == k:
            print(arr.index(arr[i]))
            break