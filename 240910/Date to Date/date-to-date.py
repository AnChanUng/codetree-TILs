m1, d1, m2, d2 = map(int, input().split())

date = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

if d2 - d1 < 0:
    result = (date[m2] + d2) - (date[m1] + d1) + 1
else:
     result = (date[m2] + d2) - (date[m1] + d1)

print(result)