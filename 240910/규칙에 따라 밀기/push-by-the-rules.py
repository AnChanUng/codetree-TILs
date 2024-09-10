a = input()
word = input()

for i in range(len(word)):
    if word[i] == 'L':
        a = a[1:] + a[0]
    
    elif word[i] == 'R':
        a = a[-1] + a[0:len(a)-1]

print(a)