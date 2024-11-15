def findx(max):
    start = 1
    n = 0
    while start <= max:
        start = start * 2
        n = n + 1
    return n


print(findx(38440000000))