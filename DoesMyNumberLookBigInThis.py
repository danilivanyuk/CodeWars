def narcissistic( value ):
    degree = len(str(value))
    values = list(str(value).split())
    total = 0
    for i in values[0]:
        a = int(i)**int(degree)
        total += a
    return True if total == value else False
