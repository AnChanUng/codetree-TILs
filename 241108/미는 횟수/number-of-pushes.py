a = input()
b = input()

if len(a) != len(b):
    print(-1)
else:
    n = 0
    flag = -1

    for i in range(len(a)):
        a = a[-1] + a[:-1]
        n += 1

        if a == b:
            flag = 1
            break

    if flag == 1:
        print(n)
    else:
        print(-1)