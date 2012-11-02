def drange(start, stop, step):
    ret = start
    while ret < stop:
        yield ret
        ret += step


