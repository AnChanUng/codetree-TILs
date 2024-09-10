s, q = input().split()

s = list(s)
q = int(q)
for _ in range(q):
    word = input().split()
    word[0] = int(word[0])
    
    if word[0] == 1:
        word[1] = int(word[1])
        word[2] = int(word[2])
        # 첫번째 문자와 두번째 문자 교환
        s[word[1]-1], s[word[2]-1] = s[word[2]-1], s[word[1]-1]        
        
        for wo in s:
            print(*wo, end="")
        print()

    elif word[0] == 2:
        
        for i in range(len(s)):
            if s[i] == word[1]:
                s[i] = word[2]
        
        for wo in s:
            print(*wo, end="")