word1 = input()
word2 = input()

array1 = ""
array2 = ""
for i in word1:
    if i.isdigit():
        array1 += "".join(i)
    
for j in word2:
    if j.isdigit():
        array2 += "".join(j)

print(int(array1) + int(array2))