a = input()
b = input()

re = False
if len(a) != len(b):
    print(-1)
else:
    for i in range(len(a)):
        res = a[i:] + a[:i]

        if res == b:
            print(i)
            re = True
            break

    if re == False:
        print(-1)