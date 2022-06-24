def maskify(cc):
    arr = ""
    for i in cc[4:]:
        i = "#"
        arr+=i
    arr += cc[-4:]
    return arr