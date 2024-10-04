n = int(input())
array = list(map(int, input().split()))

array.sort()

m = array[0] + array[-1]
print(m)