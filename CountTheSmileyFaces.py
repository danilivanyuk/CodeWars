import re
def count_smileys(arr):
    return len(list(re.findall(r'[:;][-~]?[D)]', " ".join(arr))))