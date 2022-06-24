def rot13(message):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numList = ['1','2','3','4','5','6','7','8','9','0']
    punctList = [' ', '!', '?', ',', '.', '+']
    msg_to_list = list(message)
    someList = []
    for i in msg_to_list:
        if i in numList:
            someList.append(i)
        elif i in punctList:
            someList.append(i)
        else:
            letterIndex = alphabet_upper.index(i) if i.isupper() else alphabet.index(i)
            
            if letterIndex+13>25:
                x = (letterIndex+12)-25
                newLetter = alphabet_upper[x] if i.isupper() else alphabet[x]

                someList.append(newLetter)
            else:
                newLetter = alphabet_upper[letterIndex+13] if i.isupper() else alphabet[letterIndex+13]
                someList.append(newLetter)
    res = ''
    res = ''.join(someList)

    return res



print(rot13('1TEst some'))