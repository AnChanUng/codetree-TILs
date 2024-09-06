array = []
for _ in range(5):
    number = list(input().split())
    array.append(number)

for i in range(5):
    for j in range(3):
        print(array[i][j].upper(), end = " ")
    print()