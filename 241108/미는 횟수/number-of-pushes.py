a = input()
b = input()

for i in range(len(a)):
    res = a[i:] + a[:i]
    
    if res == b:
        print(i)