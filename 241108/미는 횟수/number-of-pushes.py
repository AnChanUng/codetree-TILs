a = input()
b = input()

re = False
for i in range(len(a)):
    res = a[i:] + a[:i]

    if res == b:
        print(i)
        re = True
        break

if re == False:
    print(-1)