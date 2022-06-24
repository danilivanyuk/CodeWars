import re
def to_camel_case(text):
    a = re.split('[-_]', text)
    c = [a[0]]
    for i in range(1, len(a)):
        c.append(a[i].capitalize())
        print(c)
    x = ''.join(c)
    return x

