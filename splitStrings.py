def solution(s):
    a = []
    if len(s) % 2 != 0:
        s = s+'_'
    for i in range(len(s)):
        if i % 2 == 0:
            print(i, 'Parent')
            c = s[i]+s[i+1]
            a.append(c)
    return a

