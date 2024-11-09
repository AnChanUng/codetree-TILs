n = int(input())

total = 0
for _ in range(n):
    number = int(input())
    total += number

total = str(total)

print(total[1:] + total[0])