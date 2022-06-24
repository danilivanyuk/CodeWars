import re
# "the-stealth-warrior" gets converted to "theStealthWarrior"


def count_smileys(arr):
    return len(list(re.findall(r'[:;][-~]?[D)]', " ".join(arr))))


print(count_smileys([';]', ':0D', ';*', ':$', ';-D']))
