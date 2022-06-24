def rot13(message):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    msg_to_list = list(message)
    someList = []
    # someList.append(alphabet.index('e')+13)
    for i in msg_to_list:
        letterIndex = alphabet.index(i)
        if letterIndex+13>25:
            x = (letterIndex+13)-25
            # print('x: ', x)
            newLetterIndex = alphabet[x]
            someList.append(alphabet.index(newLetterIndex))
        else:
            someList.append(letterIndex+13)
        
    res = ''
    for i in someList:
        res += alphabet[i]
    # res.join(alphabet[x] for x in someList)
    # x = alphabet.index(msg_to_list[0])
    return res



print(rot13('test'))