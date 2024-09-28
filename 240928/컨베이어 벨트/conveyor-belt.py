n, t = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

temp1 = array1[n-1]
for i in range(n-1, 0, -1):
    array1[i] = array1[i-1]


temp2 = array2[n-1]
for i in range(n-1, 0, -1):
    array2[i] = array2[i-1]

array1[0] = temp2
array2[0] = temp1

print(array1)
print(array2)