def digital_root(n):
    a = sum(int(x)for x in str(n))
    return sum(int(x) for x in str(a))